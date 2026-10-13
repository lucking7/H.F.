"""Original ink-style extensions, with authored curves and contrasting filled/outline marks."""
from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent

def p(d,fill='none',w=2.7,**extra):
 w=round(w * (1.10 if fill=='none' else 1),3)
 attrs=' '.join(f'{k.replace("_","-")}="{v}"' for k,v in extra.items())
 return f'<path d="{d}" fill="{fill}" stroke="#000000" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {attrs}/>'
def dot(x,y,r=1.4):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#000000"/>'
def spark(x,y,a=19,b=30,solid=False,angle=0):
 d=f'M{x} {y-b} C{x+1} {y-7} {x+5} {y-1} {x+a} {y} C{x+5} {y+1} {x+1} {y+7} {x} {y+b} C{x-1} {y+7} {x-6} {y+1} {x-a} {y} C{x-6} {y-1} {x-1} {y-8} {x} {y-b} Z'
 return p(d,'#000000' if solid else 'none',2.5,transform=f'rotate({angle} {x} {y})')
def rays(items):return ''.join(p(f'M{x} {y}q{dx/2-1} {dy/2+1} {dx} {dy}',w=2.4) for x,y,dx,dy in items)
art={}
def add(slug,name,zh,shape):
    titles={'download':'Download','upload':'Upload','ai':'AI','game':'Game','balance':'Load Balance','shield':'Protection'}
    art[slug]=(titles.get(slug,name.replace(' ink','')),zh,shape)
add('smart','Smart ink','灵感',spark(120,123,52,76,False,-12)+spark(182,166,24,35,True,8)+spark(62,67,13,20,True,-9)+rays([(155,47,12,-16),(51,149,-13,14),(173,111,17,-14),(74,194,-9,12)])+dot(203,128)+dot(92,37))
add('auto','Auto ink','自动循环',p('M71 80C87 52 140 47 174 71C189 81 197 96 200 111',w=3)+p('M193 79Q194 102 206 119Q185 113 171 117Q191 100 193 79Z','#000000',1)+p('M185 168C158 198 103 205 74 179C61 168 57 153 55 138',w=3)+p('M61 171Q58 147 49 129Q69 137 86 129Q67 147 61 171Z','#000000',1)+spark(125,127,24,36,False,12)+dot(202,159)+dot(52,92))
add('direct','Direct ink','直达',p('M48 169C87 146 127 116 185 89',w=2.6)+p('M48 169C83 159 140 122 185 89C151 98 128 92 117 82Q162 88 210 69Q193 112 185 144Q184 112 185 89Z','#000000',1)+p('M78 176Q97 167 111 156',w=2.1)+spark(61,85,12,21,False,-14)+dot(153,184)+rays([(100,64,13,-10),(190,173,9,15)]))
add('proxy','Proxy ink','穿梭',p('M91 108C99 78 136 70 159 90C184 111 179 146 156 163C137 178 109 174 94 155',w=2.8)+p('M47 151C63 127 112 99 169 86Q203 78 213 89C220 104 167 141 115 159Q76 177 51 166',w=2.7)+p('M49 162Q97 158 146 133Q185 112 214 89C208 111 160 144 109 161Q68 177 49 162Z','#000000',.9)+spark(68,64,12,22,True,-6)+spark(191,185,11,17,False,16)+dot(54,114)+dot(165,47))
add('fallback','Fallback ink','备用路径',p('M50 73C85 67 120 71 142 81C174 96 155 127 120 129C88 130 84 156 108 173Q131 191 195 175',w=3)+p('M171 159Q191 166 212 168Q199 183 194 199Q192 181 171 159Z','#000000',1)+p('M48 85Q80 80 98 87',w=1.8)+spark(188,78,13,22,False,10)+spark(61,174,11,15,True,-11)+dot(161,140)+dot(117,51))
add('balance','Balance ink','平衡',p('M128 62Q126 123 130 198M82 205Q129 200 172 206',w=3)+p('M61 92Q120 98 192 88',w=2.6)+p('M72 95Q59 131 46 148Q75 170 108 148Q94 126 83 96M169 91Q160 119 142 140Q172 161 205 138Q188 120 180 90',w=2.3)+p('M47 149Q79 165 107 149Q83 183 47 149Z','#000000',.8)+p('M143 141Q173 156 204 139Q179 171 143 141Z','#000000',.8)+spark(127,58,12,18,True,-8)+spark(58,192,8,12,False,-10)+rays([(192,63,11,-10)])+dot(51,67)+dot(208,182))
add('shield','Shield ink','守护',p('M127 51C143 65 166 71 189 73Q193 126 180 157C165 185 143 204 128 210C98 194 67 157 65 124L67 77Q106 71 127 51Z',w=3)+p('M128 52Q153 73 187 73L179 93Q153 80 128 69Z','#000000',1)+spark(125,128,34,51,False,-4)+spark(205,116,10,16,True,9)+dot(56,178)+rays([(55,53,9,-10),(180,210,13,-12)]))
add('speed','Speed ink','疾行',spark(163,95,33,53,False,38)+spark(199,60,14,22,True,25)+p('M49 192Q110 137 144 114M62 209Q106 168 145 141M43 170Q97 126 128 108',w=2.7)+p('M50 192Q92 145 140 118Q110 147 50 192Z','#000000',.7)+dot(75,213)+dot(38,190)+dot(87,158)+rays([(143,48,7,-12),(204,136,10,-6)]))
add('search','Search ink','探寻',p('M90 61C120 46 153 56 166 84C182 117 164 148 140 157C108 170 78 150 71 125C64 97 69 76 90 61Z',w=3)+p('M87 76Q76 94 78 105',w=1.8)+p('M148 154Q158 161 170 176L193 207Q207 217 209 204L166 158Z','#000000',1)+spark(123,109,22,34,False,-8)+dot(196,87)+spark(48,175,9,15,True,8))
# Gestural hands connect the new functional scenes to the original magic artwork.
hand=p('M48 193Q75 187 91 193L114 181Q134 171 151 165Q166 159 170 168Q168 175 146 185L132 196Q165 198 185 188L207 177Q218 174 213 184Q190 209 161 213L119 214Q94 202 70 210L45 218',w=2.6)+p('M48 194Q75 189 92 195L116 184Q147 169 162 166Q152 181 130 193Q111 208 94 203Q75 196 48 204Z','#000000',1)
add('download','Receive ink','接收',hand+spark(130,100,27,44,False,-5)+p('M126 42Q125 56 128 64M131 135Q132 146 130 158M116 148Q125 155 130 160Q136 155 143 147',w=2.6)+dot(61,117)+dot(187,89)+spark(184,126,10,17,True,13))
add('upload','Send ink','发送',hand+spark(153,65,24,37,True,12)+p('M104 151Q111 129 128 110M116 121Q124 115 128 110Q133 116 139 124',w=2.6)+spark(67,82,10,17,False,-12)+dot(189,110)+rays([(194,51,12,-8),(156,124,13,-13)]))
add('cloud','Cloud ink','云端',p('M70 167C39 162 45 127 65 123C54 94 75 77 97 85C105 54 151 52 164 86C194 72 218 99 201 124C222 142 210 174 184 177L150 178M101 178L74 173',w=2.8)+p('M65 124Q65 110 73 101Q71 127 57 137Q51 131 65 124Z','#000000',1)+p('M67 124C59 103 75 84 95 87C86 97 92 107 78 121Z','#000000',.7)+spark(129,146,24,41,False,-5)+dot(45,79)+dot(191,54)+spark(200,197,9,14,True,5))
add('ai','Insight ink','智能洞察',p('M40 126C79 82 105 70 130 73C160 74 192 98 214 128C177 171 153 181 126 179C96 176 68 152 40 126Z',w=2.6)+p('M40 126Q73 104 91 91Q80 118 54 137Z','#000000',1)+p('M183 156Q203 140 214 128Q195 124 187 115Q193 138 183 156Z','#000000',1)+spark(128,125,29,41,False,8)+rays([(111,55,-3,-18),(155,56,7,-16),(109,196,-8,13)])+dot(69,61)+dot(188,197))
add('game','Play ink','游玩',p('M61 75L139 55L176 184L91 208Z',w=2.7)+p('M103 69L177 74L196 199L116 200Z',w=2.7)+p('M178 76L187 86L204 202L194 201Z','#000000',1)+p('M61 75L82 69L78 83L64 91Z M91 208L105 203L102 188L88 190Z M177 74L165 73L180 88Z','#000000',.7)+p('M94 125C81 137 89 158 106 160C84 167 70 142 94 125Z','#000000',.7)+spark(145,130,23,38,False,12)+spark(99,106,13,24,True,-13)+dot(153,185)+dot(196,47)+rays([(49,153,-9,8),(186,218,12,-8)]))
base='''<defs><linearGradient id="paper" x1="0" y1="0" x2=".15" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#FCFCFC"/><stop offset="1" stop-color="#E4E4E4"/></linearGradient><filter id="lift" x="-15%" y="-15%" width="130%" height="145%"><feDropShadow dx="0" dy="3.8" stdDeviation="2.5" flood-color="#000000" flood-opacity=".30"/></filter></defs><rect x="10" y="7" width="236" height="236" rx="58" fill="url(#paper)" filter="url(#lift)"/>'''
for slug,(name,zh,shape) in art.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 256 256" role="img" aria-label="{name}">{base}<g transform="translate(128 128) scale(1.025) translate(-128 -128)">{shape}</g></svg>\n'
 (HERE/'source'/f'{slug}.svg').write_text(svg)
originals=['astrology','astronomy','brightstar1','brightstar2','crystal','magic','magiccard','magicsun','star','stars']
index={'name':"LUCK's 墨线手绘图标",'description':'10 preserved original ink drawings plus 14 new organic ink-style drawings. Original PNGs are unchanged.','icons':[{'name':s,'url':f'https://raw.githubusercontent.com/lucking7/H.F./main/signal/{s}.png'} for s in originals]+[{'name':v[0],'url':f'https://raw.githubusercontent.com/lucking7/H.F./main/signal/ink/1024/{s}.png'} for s,v in art.items()]}
(ROOT/'UI-Handdrawn-Ink.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
(HERE/'manifest.json').write_text(json.dumps({'originals':originals,'extensions':[{'slug':s,'name':v[0],'meaning':v[1]} for s,v in art.items()]},ensure_ascii=False,indent=2)+'\n')
print('14 authored organic ink drawings; 24-item collection')
