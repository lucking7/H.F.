"""Render the AI accelerator icon with independent optical and semiconductor layers.

Requires numpy and Pillow. Coordinates are in final icon pixels.
"""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

size = 1440
resolution = size / 1024
grid = (np.arange(size, dtype=np.float32)+.5) / resolution
X, Y = np.meshgrid(grid, grid)
gen = np.random.default_rng(62)
grain = gen.standard_normal((size,size), dtype=np.float32)
canvas = Image.new('RGBA', (size,size))

def ramp(field, stops):
    vals, colors = zip(*stops)
    channels = list(zip(*colors))
    return np.stack([np.interp(field, vals, channel) for channel in channels], -1).astype(np.float32)

def color(hex):
    return [int(hex[j:j+2],16) for j in (0,2,4)]

def mix(first, second, weight):
    return first + (second - first) * weight[...,None]

def layer(fill, alpha):
    image = np.zeros((size,size,4), np.uint8)
    image[:,:,:3] = np.uint8(np.clip(fill,0,255)+.49)
    image[:,:,3] = np.uint8(np.clip(alpha,0,1)*255+.49)
    canvas.alpha_composite(Image.fromarray(image))

def highlight(f, width):
    return np.exp(-.5 * (f/width)**2)

def sqrect(x,y, w,h, radius):
    qx=np.abs(x)-(w/2-radius)
    qy=np.abs(y)-(h/2-radius)
    return np.hypot(np.maximum(qx,0),np.maximum(qy,0))+np.minimum(np.maximum(qx,qy),0)-radius

def shell_shape(vertical=0):
    x = (X-512)/410
    y = (Y-506-vertical)/404
    return ((np.abs(x)**4.65 + np.abs(y)**4.65)**(1/4.65)-1)*405

shadow = np.asarray(Image.fromarray(np.uint8(np.clip((5-shell_shape(11))*100,0,255))).filter(ImageFilter.GaussianBlur(8*resolution)),np.float32)/255
layer(color('01030b'), shadow*(.065+.21*(.4+.6*(Y/1024))))

d = shell_shape(9)
brushed = grain*.64 + highlight(np.sin(Y*6),.08)*.75
rim = ramp(.57+(.40*(-X+Y)/850), [(0,color('313841')),(.37,color('1c242f')),(.62,color('2b323f')),(1,color('080b12'))])
rim += (28*highlight(d+1.8,2.5)*(X+Y)/2048 + brushed)[:,:,None]
layer(rim,.5-d*resolution)

d = shell_shape(0)
x = (X-515)/418
y = (Y-509)/418
slope = (x + y*.9)
environment = highlight(slope+.69,.27) * (1-.42*highlight(x+.55,.22))
tile = ramp(environment, [(0,color('090b12')),(.48,color('161f2c')),(1,color('29353f'))])
tile += (highlight(x+.28,.55)*highlight(y+.48,.20)*8 + grain*.47)[:,:,None]
strip = highlight(y+.785+.20*x*x,.031) * highlight(x+.1,.59)
tile += strip[:,:,None] * np.array([15,19,30])
edge = highlight(d+12,6.3)
tile += edge[:,:,None] * ramp((x+y)/2, [(-1,color('576374')),(-.4,color('2a354d')),(.47,color('12121d')),(1,color('344868'))])
tile += (highlight(d+1.5,1)*(24+16*highlight(x+.7,.47)) + highlight(d+23,1.9)*10)[:,:,None]
interference = [(-.2,color('0d1732')),(.15,color('142b76')),(.28,color('216bcb')),(.43,color('4dbac6')),(.59,color('9c98b7')),(.72,color('dca36d')),(.84,color('9c5569')),(1.08,color('11121f'))]
for flip, power in ((1, .85),(-1,.69)):
    bearing = np.arctan2(-flip*y, flip*x) - .82
    reflected_depth = d + 11 + 23*np.sin(bearing*3)
    angle = .52 + reflected_depth/37 + .72*bearing
    chroma = ramp(angle,interference)
    intensity = highlight(bearing,.30) * highlight(reflected_depth,21) * power
    tile = mix(tile,chroma,intensity)
    secondary = .22 + (reflected_depth + 20)/23
    tile = mix(tile,ramp(secondary,interference),highlight(bearing+.07,.19)*highlight(reflected_depth+24,5)*.45)
layer(tile,.5-d*resolution)

ang = math.radians(-12.5)
cos, sin = math.cos(ang), math.sin(ang)
tilt = .931
cx, cy = 512., 501.

def world(x,y,z):
    return ((cx+x*cos-y*sin)*resolution, (cy+(x*sin+y*cos)*tilt-z)*resolution)

def local(z):
    x,y = X-cx,(Y-cy+z)/tilt
    return x*cos+y*sin, -x*sin+y*cos

def reflect(d, x, y, base, bevel, intensity):
    # The horizontal surfaces and machined edges receive different studio reflections.
    edge = highlight(d+bevel*.44,bevel*.33)
    light = np.clip(.67-.57*(x+y*.73)/460,.10,1.0)
    brushed = 1.2*grain + .33*np.sin(x*8.6) + .37*np.sin(y*9.7)
    return base + ((edge*light*intensity) + brushed)[...,None]

def slab(z,w,h,radius,stops,bevel=4,intensity=42, offset_x=0,offset_y=0):
    x,y=local(z)
    x-=offset_x
    y-=offset_y
    d=sqrect(x,y,w,h,radius)
    shine = .5-.43*(.64*x+.78*y)/290
    value=ramp(shine, stops)
    value=reflect(d,x,y,value,bevel,intensity)
    layer(value,.5-d*resolution)

# Physical thickness extends downwards, then each face catches a different softbox.
pack_x,pack_y=local(-12)
package_shadow=np.asarray(Image.fromarray(np.uint8(np.clip((3-sqrect(pack_x,pack_y,562,548,25))*85,0,255))).filter(ImageFilter.GaussianBlur(13*resolution)),np.float32)/255
layer(color('000106'), package_shadow*.69)
slab(-12,562,551,22, [(0,color('080c10')),(1,color('282a34'))],8,65)
slab(-6,561,550,22, [(0,color('312719')),(1,color('806443'))],4,65)
slab(0,560,548,21, [(0,color('1a2628')),(1,color('364a49'))],7,60)
slab(3,552,540,19, [(0,color('151e22')),(.42,color('223332')),(1,color('415852'))],4,44)

# Their narrow width and tapered spacing are drawn in package object coordinates.
def within(z):
    surface = Image.new('RGBA',(size,size))
    return surface,ImageDraw.Draw(surface),lambda x,y:world(x,y,z)

def path(draw, to_canvas, points, tone, width=1.5):
    draw.line([to_canvas(x,y) for x,y in points], fill=tone,width=max(1,round(width*resolution)),joint='curve')

def rect(draw, to_canvas, x,y,w,h,tone):
    draw.polygon([to_canvas(x-w/2,y-h/2),to_canvas(x+w/2,y-h/2),
                  to_canvas(x+w/2,y+h/2),to_canvas(x-w/2,y+h/2)],fill=tone)

copper=(145,112,66,241)
tile_art, draw, to_canvas = within(4)
for flip in (-1,1):
    for i in range(31):
        i-=15
        x=i*6.25
        fan=i*6.76
        xt=i*9.25
        y=215+abs(i)*.30
        dy=(i%7)*1.0
        path(draw,to_canvas,[(x,flip*186),(x,flip*(193+dy)),(fan,flip*(204+dy)),(fan,flip*y),(xt,flip*(238+dy)),(xt,flip*257)],copper)
        rect(draw,to_canvas,xt,flip*256,5.7,8.4,(183+(i%7)*4,144+(i%7)*4,85+(i%7)*3,255))
        x=i*7.2
        fan=i*8.9
        y=240+abs(i)*.7
        path(draw,to_canvas,[(flip*218,x),(flip*232,x),(flip*y,fan),(flip*263,fan)],copper,1.3)
        rect(draw,to_canvas,flip*265,fan,8,5.7,(168+(i%7)*4,133+(i%7)*3,83+(i%7)*2,255))
    for i in range(7):
        for y in (-215-i*4, 214+i*4):
            x=flip*(203+i*7.6)
            rect(draw,to_canvas,x,y+2,9,6,(21,24,24,255))
            rect(draw,to_canvas,x,y,10,6.5,(130,139,124,255))
            rect(draw,to_canvas,x,y,4.7,7,(109+(i%4)*10,79+(i%4)*13,51+(i%4)*10,255))
    for y in (-232,232):
        x=flip*248
        path(draw,to_canvas,[(x-flip*21,y),(x,y),(x,y-math.copysign(20,y))],(186,146,91,255),2.2)
canvas.alpha_composite(tile_art)

slab(5,472,399,15, [(0,color('141719')),(1,color('252b30'))],5,37)
slab(8,467,394,12, [(0,color('493728')),(1,color('8a7254'))],4,50)
slab(11,464,390,11, [(0,color('212226')),(1,color('313a41'))],3,28)

# Shelf of visible gold connections at opposite edges.
c4, draw, to_canvas = within(12)
for side in (-1,1):
    for i in range(-19,20):
        rect(draw,to_canvas,i*9+2,side*183,4.2,5.2,(168+(i%6)*12,127+(i%6)*8,77+(i%6)*4,255))
canvas.alpha_composite(c4)

# Four stacks of memory surrounding a single exposed compute die.
for side in (-1,1):
    sx=side*173
    for sy in (-91,91):
        slab(10,77,159,6, [(0,color('12151b')),(1,color('353b41'))],4,50,sx,sy)
        for z in [12,17,22]:
            slab(z,73,155,5, [(0,color('24252c')),(1,color('767480'))],4,55,sx,sy)
            slab(z+2,72,154,5, [(0,color('2b2d36')),(1,color('b0aeb6'))],3,84,sx,sy)
        slab(27,71,152,5, [(0,color('434853')),(.51,color('6d7a83')),(.76,color('9faeb1')),(1,color('b7c1c3'))],4,74,sx,sy)

hbm,draw,to_canvas=within(28)
for side in (-1,1):
    sx=side*173
    for sy in (-91,91):
        for j in range(38):
            y=sy+(j-18.5)*3.6
            rect(draw,to_canvas,sx,y,49,.65,(214,219,220,55+(j%6)*10))
            rect(draw,to_canvas,sx,y+.9,49,.4,(23,34,41,40+(j%5)*8))
        rect(draw,to_canvas,sx,sy,1,102,(173,183,179,81))
canvas.alpha_composite(hbm)

slab(10,271,363,7, [(0,color('1e1a25')),(1,color('393745'))],7,65)
slab(15,269,361,5, [(0,color('553e45')),(.55,color('9d787a')),(1,color('ada5ac'))],4,65)
slab(21,268,360,5, [(0,color('3d354f')),(.52,color('8b677b')),(.82,color('a68c93')),(1,color('ded1be'))],4,95)

sx,sy=local(27)
die=sqrect(sx,sy,265,357,5)
phase=.51+(.86*sx+.44*sy)/329+.110*np.sin(sy/220)
diecolor=ramp(phase, [(0,color('846771')),(.28,color('a17485')),(.45,color('92648b')),(.60,color('78678e')),
                       (.70,color('927eb4')),(.79,color('b795a4')),(.95,color('e4c8a3'))])
diecolor += (highlight(sy+.82*sx-50,85)*13+highlight(die+2,1.8)*36 + grain*1.6)[:,:,None]
layer(diecolor,.5-die*resolution)

logic,draw,to_canvas=within(27.1)
rnd=np.random.default_rng(301)
for side in (-1,1):
    for row in range(12):
        y=(row-5.5)*25.8
        x=side*68
        rect(draw,to_canvas,x,y,88,20.4,(91,61,92,175))
        rect(draw,to_canvas,x,y-4.3,88,7.5,(83,62,106,180))
        rect(draw,to_canvas,x,y+8.7,87,2.8,(213,155,157,146))
        rect(draw,to_canvas,x+side*45,y,2,20,(205,167,181,139))
        for col in range(35):
            xline=x+(col-17)*2.3
            v=int(rnd.integers(0,4))*13
            rect(draw,to_canvas,xline,y-.46,float(rnd.uniform(.40,.9)),float(rnd.uniform(6,17)),(191+v,143+v,162+v,113+v))
        for subrow in (0,1,2):
            xline=x-side*37+subrow*side*12
            rect(draw,to_canvas,xline,y,5.1,16,(203,159,166,133))
    for j in range(86):
        x=side*(119+(j%4)*1.9)
        y=(j-42.5)*3.8
        rect(draw,to_canvas,x,y,2.4,1.4,(221,162+(j%5)*13,152+(j%5)*10,180))
for j in range(20):
    y=(j-9.5)*15
    rect(draw,to_canvas,0,y,35,11.5,(81,66,108,191))
    rect(draw,to_canvas,0,y,21,7.1,(129,107,154,185))
    for k in range(13):
        x=(k-6)*1.59
        rect(draw,to_canvas,x,y,0.57,5.1,(218,182,200,140))
for side in (-1,1):
    for j in range(4):
        path(draw,to_canvas,[(-123,side*(158+j*2)),(123,side*(158+j*2))],(219-j*20,168-j*13,149-j*9,135),.62)
    rect(draw,to_canvas,0,side*169,246,3,(215,162,135,170))
    for i in range(95):
        x=(i-47)*2.58
        rect(draw,to_canvas,x,side*171.5,1.0,5.5,(242,179,147,110+(i%4)*20))
canvas.alpha_composite(logic)

canvas = canvas.resize((1024,1024),Image.Resampling.LANCZOS)
canvas.save(Path(__file__).resolve().parents[1] / 'png' / 'ai-silicon.png', optimize=True)
