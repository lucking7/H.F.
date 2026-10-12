from pathlib import Path
import json,math,html
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
pale={'select':'#EBE3FF','direct':'#C7F4DD','global':'#ABF1FC','rules':'#CBD0FF','reject':'#FFE1E4','ai':'#E9DCFF','stream':'#FFDCCC','cloud':'#DAEDFF','final':'#E3EDF6','game':'#E8DAFF','dns':'#B9EFF0'}
# Record only author-controlled geometry and colors; no Apple icon artwork is redistributed.
for row in rows:
 slug=row['slug'];ld=D/'layers'/slug;ld.mkdir(exist_ok=True)
 for layer in ['back','front']:
  body=row[layer];color=row['bottom'] if layer=='back' else pale.get(slug,row['top'])
  (ld/(layer+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 256 256"><g fill="{color}" fill-rule="evenodd">{body}</g></svg>\n')
 if row['accent']:(ld/'accent.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 256 256">{row["accent"]}</svg>\n')
 (ld/'background.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024"><rect width="1024" height="1024" fill="#F5F7FB"/></svg>\n')
 # Static material simulation: separate depth shadow, color-bearing solid layer, translucent front, crisp specular edge.
 defs=f'''<defs>
 <linearGradient id="plate" x1="0" y1="0" x2=".2" y2="1"><stop stop-color="#FFFFFF"/><stop offset=".55" stop-color="#F4F6FA"/><stop offset="1" stop-color="#E0E5ED"/></linearGradient>
 <radialGradient id="tint" cx=".5" cy=".42" r=".65"><stop stop-color="{row['top']}" stop-opacity=".18"/><stop offset="1" stop-color="{row['top']}" stop-opacity="0"/></radialGradient>
 <linearGradient id="body" x1="0" y1="0" x2=".25" y2="1"><stop stop-color="{row['top']}"/><stop offset=".55" stop-color="{row['bottom']}"/><stop offset="1" stop-color="{row['bottom']}"/></linearGradient>
 <linearGradient id="glass" x1="0" y1="0" x2=".2" y2="1"><stop stop-color="#FFFFFF" stop-opacity=".75"/><stop offset=".22" stop-color="{row['top']}" stop-opacity=".92"/><stop offset=".68" stop-color="{row['bottom']}" stop-opacity=".91"/><stop offset="1" stop-color="{row['bottom']}"/></linearGradient>
 <linearGradient id="rim" x1="0" y1="0" x2=".3" y2="1"><stop stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".4" stop-color="#FFFFFF" stop-opacity=".24"/><stop offset="1" stop-color="{row['bottom']}" stop-opacity=".55"/></linearGradient>
 <filter id="shadow" x="-35%" y="-35%" width="170%" height="180%"><feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="{row['bottom']}" flood-opacity=".3"/></filter>
 <filter id="frontShadow" x="-35%" y="-35%" width="170%" height="180%"><feDropShadow dx="0" dy="3" stdDeviation="2" flood-color="{row['bottom']}" flood-opacity=".3"/></filter>
 <clipPath id="mask"><rect x="8" y="8" width="240" height="240" rx="53"/></clipPath>
 <clipPath id="frontMask">{row['front']}</clipPath>
 </defs>'''
 # Keep every glyph within the shared safe zone by scaling about the optical center.
 glyph=f'''<g transform="translate(128 128) scale(.87) translate(-128 -128)" fill-rule="evenodd">
 <g id="depth" fill="url(#body)" filter="url(#shadow)">{row['back']}</g>
 <g id="foreground" fill="{pale.get(slug,'url(#glass)')}" stroke="url(#rim)" stroke-width="1.15" stroke-linejoin="round" filter="url(#frontShadow)">{row['front']}</g>
 <g id="accent">{row['accent']}</g>
 </g>'''
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 256 256" role="img" aria-label="{html.escape(row['name'])}">{defs}
 <rect x="8" y="8" width="240" height="240" rx="53" fill="url(#plate)"/>
 <g clip-path="url(#mask)"><rect x="8" y="8" width="240" height="240" fill="url(#tint)"/>{glyph}</g>
 <rect x="8.5" y="8.5" width="239" height="239" rx="52.5" fill="none" stroke="url(#rim)" stroke-width="1"/>
 </svg>'''
 (D/'source'/(slug+'.svg')).write_text(svg+'\n')
manifest=[{k:v for k,v in row.items() if k not in ['back','front','accent']} for row in rows]
(D/'manifest.json').write_text(json.dumps({'title':'Prism · Strategy Icons','size':1024,'icons':manifest},ensure_ascii=False,indent=2)+'\n')
(R/'Strategy.json').write_text(json.dumps({'name':"LUCK's 策略组图标 · Prism",'description':'24 original strategy icons inspired by layered glass material. Static PNG exports; editable SVG and unbaked layer assets included.','icons':[{'name':i['name'],'url':f'https://raw.githubusercontent.com/lucking7/H.F./main/strategy/png/{i["slug"]}.png'} for i in rows]},ensure_ascii=False,indent=2)+'\n')
print('Authored',len(rows),'distinct layered icons')
small_index=json.loads((R/'Strategy.json').read_text())
small_index['name'] += ' (144px)'
for icon in small_index['icons']:icon['url']=icon['url'].replace('/png/','/144px/')
(R/'Strategy144px.json').write_text(json.dumps(small_index,ensure_ascii=False,indent=2)+'\n')
