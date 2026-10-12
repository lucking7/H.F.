from pathlib import Path
import json,math,html
import xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[2];D=R/'strategy';D.mkdir(exist_ok=True)
for p in ['source','png','144px','layers']:(D/p).mkdir(exist_ok=True)
# Each icon is authored as filled, scalable geometry in a shared 256-unit grid.
def path(d,**a):return '<path d="'+d+'" '+attrs(a)+'/>'
def attrs(a):return ' '.join(k.replace('_','-')+'="'+str(v)+'"' for k,v in a.items())
def rect(x,y,w,h,rx=0,**a):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '+attrs(a)+'/>'
def circle(x,y,r,**a):return f'<circle cx="{x}" cy="{y}" r="{r}" '+attrs(a)+'/>'
def poly(points,**a):return '<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'" '+attrs(a)+'/>'
def star(cx,cy,outer,inner,n=5):return poly([(cx+math.cos(-math.pi/2+i*math.pi/n)*(outer if i%2==0 else inner),cy+math.sin(-math.pi/2+i*math.pi/n)*(outer if i%2==0 else inner)) for i in range(n*2)])
rows=[]
def add(slug,label,zh,top,bottom,back,front,accent='',meaning=''):
 rows.append(dict(slug=slug,name=label,zh=zh,top=top,bottom=bottom,back=back,front=front,accent=accent,meaning=meaning))
white='fill="#FFFFFF" fill-opacity=".88"'
# Small accent highlights use filled shapes, never text or emoji.
add('star','Star','收藏','#FFD65B','#ED8B16',star(140,138,76,35),star(119,114,72,33),path('M119 42 128 104 188 91 146 126 161 181 119 149Z',fill='#FFF6CB',fill_opacity='.36'),'五角星，收藏与优选')
petals=''.join(rect(91,44,74,112,35,transform=f'rotate({a} 128 128)') for a in [0,90,180,270])
add('smart','Smart','智能选择','#52E6DD','#008FAB',petals,rect(79,79,98,98,30,transform='rotate(45 128 128)'),path('M128 88 138 118 168 128 138 138 128 168 118 138 88 128 118 118Z',fill='#FFFFFF',fill_opacity='.92'),'四瓣感应器与中心星芒，智能选择')
add('auto','Auto','自动测速','#6CBBFF','#2359E9',path('M51 117A78 78 0 0 1 190 72L205 56V118H145L163 99A43 43 0 0 0 84 117Z'),path('M205 139A78 78 0 0 1 66 184L51 200V138H111L93 157A43 43 0 0 0 172 139Z'),circle(128,128,16,fill='#EFF9FF',fill_opacity='.9'),'双向循环箭头，自动探测')
add('select','Select','手动选择','#B9A3FF','#6D42D7',rect(54,54,146,150,35),path('M85 78V177L111 155 128 193 152 182 135 146 172 145Z'),circle(177,77,13,fill='#FFFFFF',fill_opacity='.85'),'指针与选择面板，手动切换')
add('fallback','Fallback','故障转移','#FFB96D','#E56727',path('M54 61H139V94H87V182H54Z')+path('M119 46 172 78 119 110Z'),path('M103 162H154V103H187V195H103Z')+path('M120 137 70 179 120 218Z'),circle(69,69,16,fill='#FFF5DD',fill_opacity='.85'),'转向备用路径的双折线箭头')
add('load-balance','Load Balance','负载均衡','#6DDEBE','#138D75',path('M111 47H145V101H201V133H55V101H111Z'),rect(42,154,48,49,15)+rect(104,154,48,49,15)+rect(166,154,48,49,15),rect(118,126,20,40,8,fill='#EBFFF8',fill_opacity='.9'),'一入三出，负载分配')
add('direct','Direct','直连','#75DBA0','#20924D',rect(47,79,163,100,40),path('M76 112H135V86L186 129 135 171V146H76Z'),'', '直达箭头，直接连接')
add('proxy','Proxy','代理','#75B1FF','#3258CB',rect(43,87,99,105,27),rect(113,55,99,105,27),path('M90 128H153V111L178 135 153 159V142H90Z',fill='#FFFFFF',fill_opacity='.9'),'相互覆盖的网络节点与穿越箭头')
add('global','Global','全局','#58D7EF','#087EA8',circle(128,130,82),path('M69 98 84 79 112 75 121 85 115 99 128 109 113 124 110 141 93 136 88 117 74 115Z M119 137 139 144 149 160 138 183 124 197 117 172 111 153Z M139 83 165 81 188 103 180 119 158 122 151 107 134 100Z'),'','球体与抽象大陆，全局路由')
add('rules','Rules','规则分流','#ADB4FF','#5962C7',rect(54,43,144,171,29),rect(80,81,91,15,7)+rect(80,119,62,15,7)+rect(80,157,78,15,7),circle(175,170,29,fill='#FFFFFF',fill_opacity='.91')+path('M157 171 164 164 171 171 186 153 193 159 172 185Z',fill='#5D63CB'),'规则文档与完成标记')
add('reject','Reject','拦截','#FF8D94','#D73B4C',path('M91 43H165L213 91V165L165 213H91L43 165V91Z'),path('M91 70 186 165 166 185 71 90Z'),'', '八边形禁行标记')
add('dns','DNS','域名解析','#7FDCDD','#208D98',rect(49,49,158,69,24)+rect(49,137,158,69,24),circle(78,83,10)+circle(78,171,10)+rect(105,74,68,17,8)+rect(105,162,68,17,8),circle(184,193,23,fill='#DFFFFA',fill_opacity='.94'),'双层解析服务器')
add('speed','Speed','速度优先','#FFC267','#E58816',path('M46 179A90 90 0 1 1 210 179L183 165A59 59 0 1 0 73 165Z'),path('M117 155 176 77 145 170Z')+circle(128,163,20),circle(128,163,8,fill='#FFF4CD',fill_opacity='.92'),'测速表盘与指针')
add('privacy','Privacy','隐私保护','#82B9FF','#3A5CCA',path('M128 36 203 65V120C203 170 166 202 128 220 90 202 53 170 53 120V65Z'),path('M91 109V91A37 37 0 0 1 165 91V109H148V91A20 20 0 0 0 108 91V109Z')+rect(86,107,84,69,19),circle(128,133,8,fill='#EEF5FF',fill_opacity='.95')+rect(124,138,8,17,3,fill='#EEF5FF',fill_opacity='.95'),'盾牌与锁，隐私和安全')
add('stream','Stream','流媒体','#FF9A7A','#E75235',rect(41,68,174,132,34),path('M109 92Q103 88 103 97V174Q103 182 111 177L175 138Q183 134 175 129Z'),rect(75,44,110,15,7,fill='#FFC7B0',fill_opacity='.7'),'视频播放卡片')
add('ai','AI','人工智能','#C79CFF','#8245CA',rect(63,63,130,130,34)+''.join(rect(44,83+i*36,18,13,6)+rect(194,83+i*36,18,13,6)+rect(83+i*36,44,13,18,6)+rect(83+i*36,194,13,18,6) for i in range(3)),path('M128 85 138 117 171 128 138 139 128 172 117 139 85 128 117 117Z'),'', '芯片与计算星核，AI 服务')
add('search','Search','搜索','#6AC8FF','#247CB9',path('M166 148 216 198Q222 206 213 215Q204 224 195 216L146 166Z'),path('M117 44A74 74 0 1 0 117 192A74 74 0 0 0 117 44ZM117 75A43 43 0 1 1 117 161A43 43 0 0 1 117 75Z',fill_rule='evenodd'),'', '放大镜，搜索服务')
add('social','Social','社交','#FFA2CC','#CB4585',path('M43 67Q43 46 67 46H163Q186 46 186 69V126Q186 148 163 148H105L68 174V148H67Q43 148 43 126Z'),path('M103 116Q103 96 127 96H197Q218 96 218 119V166Q218 188 196 188H191V211L159 188H127Q103 188 103 167Z'),circle(144,142,7,fill='#FFE7F5')+circle(169,142,7,fill='#FFE7F5')+circle(194,142,7,fill='#FFE7F5'),'交叠对话气泡，社交服务')
add('game','Game','游戏','#AE9AFF','#7050C8',path('M86 68H170Q196 68 207 111L221 166Q226 195 202 201 183 206 162 170H94Q73 206 54 201 30 194 36 166L49 112Q60 68 86 68Z'),rect(62,119,49,15,5)+rect(79,102,15,49,5),circle(173,112,10,fill='#F3ECFF')+circle(193,135,10,fill='#F3ECFF'),'游戏手柄，低延迟游戏')
add('work','Work','工作','#83C2DD','#3A799D',path('M89 79V60Q89 42 107 42H149Q167 42 167 60V79H148V64H108V79Z')+rect(42,78,172,130,27),rect(43,107,170,50,13),rect(116,132,24,29,7,fill='#EEFBFF',fill_opacity='.94'),'公文包，工作服务')
add('download','Download','下载','#6ACFDB','#178B9B',path('M50 155H79V184H177V155H206V192Q206 215 182 215H74Q50 215 50 192Z'),path('M110 42H146V121H179L128 173 77 121H110Z'),'', '下载箭头与托盘')
add('update','Update','更新','#91CEA3','#388656',path('M53 97A84 84 0 0 1 194 73L209 58V119H148L169 98A50 50 0 0 0 84 113Z'),path('M203 160A84 84 0 0 1 62 184L47 199V138H108L87 159A50 50 0 0 0 172 144Z'),path('M118 99H140V137H156L129 166 102 137H118Z',fill='#ECFFF1',fill_opacity='.96'),'双循环箭头与状态点，系统更新')
add('cloud','Cloud','云服务','#8DCBFF','#3C85C8',path('M65 193A44 44 0 0 1 60 105A68 68 0 0 1 190 98A48 48 0 0 1 190 193Z'),path('M125 104 92 144H112V184H144V144H166Z'),'', '云与上传箭头，云端同步')
add('final','Final','兜底','#A6B8C9','#546B84',circle(128,128,83),path('M80 131 111 162 181 88 199 108 111 201 60 151Z'),'', '终点确认，默认兜底策略')
# V2: bold single-subject relief, inspired by the supplied monochrome and coral examples.
for folder in ['color', 'color-144px']:(D/folder).mkdir(exist_ok=True)
N='http://www.w3.org/2000/svg'
E.register_namespace('',N)
def solid(fragment,color):
    root=E.fromstring('<svg xmlns="'+N+'">'+fragment+'</svg>')
    for node in root.iter():
        if node is root:continue
        node.set('fill',color)
        for key in ['fill-opacity','stroke','stroke-width','stroke-linejoin','stroke-linecap']:
            node.attrib.pop(key,None)
    return ''.join(E.tostring(c,encoding='unicode') for c in root)
# Foreground cutouts clarify meaning without tiny gloss or decoration.
glyphs={}
boxes={}
for row in rows:
    k=row['slug'];back=row['back'];front=row['front'];cut='';detail=''
    if k=='star':back=star(128,128,91,41);front=''
    elif k=='smart':back=star(128,128,94,34,4);front=''
    elif k in ['direct','select']:back=front;front=''
    elif k in ['global','rules','reject','dns','ai','stream','game','cloud','final']:
        cut=front
    elif k=='update':back+=row['accent']
    elif k=='game':cut=front+circle(173,112,10)+circle(193,135,10)
    elif k=='privacy':
        cut=path('M100 112V95A28 28 0 0 1 156 95V112H148V95A20 20 0 0 0 108 95V112Z')+rect(94,110,68,58,13)
    elif k=='work':
        cut=rect(116,131,24,30,6)
    elif k=='proxy':
        back=rect(49,84,104,113,28)
        front=rect(109,44,104,113,28)
        detail=path('M86 122H153V104L184 133 153 162V144H86Z')
    elif k=='social':cut=circle(142,144,6)+circle(166,144,6)+circle(190,144,6)
    if k not in ['proxy','social']:
        if k not in ['direct','select','star','smart'] and not cut:back+=front
        front=''
    glyphs[k]=(back,front,cut,detail)
boxes.update({
 'star':(37,37,219,211),'smart':(34,34,222,222),'auto':(51,44,205,212),
 'select':(85,78,172,193),'fallback':(54,46,187,218),'load-balance':(42,47,214,203),
 'direct':(76,86,186,171),'proxy':(49,44,213,197),'global':(46,48,210,212),
 'rules':(54,43,198,214),'reject':(43,43,213,213),'dns':(49,49,207,206),
 'speed':(38,42,218,184),'privacy':(53,36,203,220),'stream':(41,68,215,200),
 'ai':(44,44,212,212),'search':(43,44,218,218),'social':(43,46,218,211),
 'game':(35,68,222,203),'work':(42,42,214,208),'download':(50,42,206,215),
 'update':(47,44,209,212),'cloud':(34,53,238,193),'final':(45,45,211,211)})
for row in rows:
    slug=row['slug'];back,front,cut,detail=glyphs[slug]
    x0,y0,x1,y1=boxes[slug];scale=186/max(x1-x0,y1-y0)
    transform=f'translate(128 127) scale({scale:.7f}) translate({-(x0+x1)/2} {-(y0+y1)/2})'
    # Each subject has a graphite-on-porcelain and ivory-on-color appearance.
    for theme in ['light','color']:
        colored=theme=='color';bg0=row['bottom'] if colored else '#FFFFFF';bg1=row['bottom'] if colored else '#ECEEF1'
        tone0='#FFFFFF' if colored else '#17191C';tone1='#EBECED' if colored else '#707276'
        rim='#FFFFFF' if colored else '#35373A'
        defs=f'''<defs>
        <linearGradient id="base" x2="0" y2="1"><stop stop-color="{bg0}"/><stop offset=".55" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>
        <linearGradient id="sculpt" x1="0" y1="0" x2=".15" y2="1"><stop stop-color="{tone0}"/><stop offset=".35" stop-color="{tone0}"/><stop offset="1" stop-color="{tone1}"/></linearGradient>
        <linearGradient id="fade" x2="0" y2="1"><stop offset=".48" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="{'.28' if colored else '.38'}"/></linearGradient>
        <linearGradient id="edge" x2="0" y2="1"><stop stop-color="#FFFFFF" stop-opacity=".85"/><stop offset=".45" stop-color="#FFFFFF" stop-opacity=".1"/><stop offset="1" stop-color="#47505E" stop-opacity=".15"/></linearGradient>
        <filter id="relief" x="-25%" y="-25%" width="150%" height="160%"><feDropShadow dx="0" dy="3.6" stdDeviation="2.6" flood-color="{row['bottom'] if colored else '#35383D'}" flood-opacity="{'.23' if colored else '.18'}"/></filter>
        <mask id="glyph" maskUnits="userSpaceOnUse" x="0" y="0" width="256" height="256"><g transform="{transform}">{solid(back,'#FFFFFF')}{solid(cut,'#000000')}</g></mask>
        <mask id="front-glyph" maskUnits="userSpaceOnUse" x="0" y="0" width="256" height="256"><g transform="{transform}">{solid(front,'#FFFFFF')}{solid(cut,'#000000')}</g></mask>
        <clipPath id="tile"><rect x="8" y="8" width="240" height="240" rx="54"/></clipPath>
        </defs>'''
        # Shadow receives the same holes as the silhouette, so glyphs remain crisp relief objects.
        symbol=f'<g filter="url(#relief)"><rect width="256" height="256" fill="url(#sculpt)" mask="url(#glyph)"/></g>'
        if front:symbol+='<g filter="url(#relief)"><rect width="256" height="256" fill="url(#sculpt)" mask="url(#front-glyph)"/></g>'
        if detail:symbol+=f'<g transform="{transform}">{solid(detail,bg0)}</g>'
        svg=f'''<svg xmlns="{N}" width="1024" height="1024" viewBox="0 0 256 256" role="img" aria-label="{html.escape(row['name'])}">{defs}
        <rect x="8" y="8" width="240" height="240" rx="54" fill="url(#base)"/>
        <g clip-path="url(#tile)">{symbol}<rect x="8" y="8" width="240" height="240" fill="url(#fade)"/></g>
        <rect x="8.6" y="8.6" width="238.8" height="238.8" rx="53.4" fill="none" stroke="url(#edge)" stroke-width="1.2"/>
        </svg>'''
        source=D/'source'/(slug+('-color' if colored else '')+'.svg');source.write_text(svg+'\n')
    # Clean vector geometry for use in a real native icon editor. No enclosure or baked light.
    ld=D/'layers'/slug
    for old in ld.glob('*.svg'):old.unlink()
    raw=f'<svg xmlns="{N}" width="1024" height="1024" viewBox="0 0 256 256"><defs><mask id="shape" maskUnits="userSpaceOnUse" x="0" y="0" width="256" height="256"><g transform="{transform}">{solid(back,"#FFFFFF")}{solid(front,"#FFFFFF")}{solid(cut,"#000000")}{solid(detail,"#000000")}</g></mask></defs><rect width="256" height="256" fill="#202226" mask="url(#shape)"/></svg>'
    (ld/'glyph.svg').write_text(raw+'\n')
    (ld/'background.svg').write_text(f'<svg xmlns="{N}" width="1024" height="1024"><rect width="1024" height="1024" fill="#F7F7F8"/></svg>\n')
manifest=[{k:v for k,v in row.items() if k not in ['back','front','accent']} for row in rows]
(D/'manifest.json').write_text(json.dumps({'title':'Relief · Strategy Icons','version':2,'size':1024,'appearances':['light','color'],'icons':manifest},ensure_ascii=False,indent=2)+'\n')
for file,folder,label in [('Strategy.json','png','Relief'),('Strategy144px.json','144px','Relief (144px)'),('StrategyColor.json','color','Relief Color'),('StrategyColor144px.json','color-144px','Relief Color (144px)')]:
    (R/file).write_text(json.dumps({'name':"LUCK's 策略组图标 · "+label,'description':'24 original large relief symbols. Static previews; editable SVG source included.','icons':[{'name':i['name'],'url':f'https://raw.githubusercontent.com/lucking7/H.F./main/strategy/{folder}/{i["slug"]}.png'} for i in rows]},ensure_ascii=False,indent=2)+'\n')
print('Authored 24 relief icons in two appearances')
