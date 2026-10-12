#!/usr/bin/env python3
"""Build original, deterministic SVG icon families. Run from the repository root."""
from pathlib import Path
import json

# Both families share functional geometry, not third-party brand marks.
icons={
'shield':('Protection','teal','<path d="M128 48 Q156 70 184 73 V127 Q180 171 128 204 Q76 171 72 127 V73 Q100 70 128 48Z"/><path class="detail" d="m98 123 22 23 42-46"/>'),
'key':('Credentials','gold','<circle cx="100" cy="92" r="31"/><path d="m122 115 62 62 m-20-20-17 17 m2-32-17 17"/><circle class="detail" cx="94" cy="86" r="8"/>'),
'link':('Link','blue','<path d="m115 154-13 13a29 29 0 0 1-41-41l32-32a29 29 0 0 1 42 1 m6 7 13-13a29 29 0 0 1 41 41l-32 32a29 29 0 0 1-42-1"/><path class="detail" d="m102 154 52-52"/>'),
'route':('Routing','teal','<path d="M65 128h47q17 0 28-18l26-42 M112 128q17 0 28 18l26 42"/><circle cx="62" cy="128" r="11"/><circle cx="174" cy="56" r="11"/><circle cx="174" cy="200" r="11"/>'),
'server':('Server','blue','<rect x="59" y="64" width="138" height="52" rx="15"/><rect x="59" y="140" width="138" height="52" rx="15"/><path class="detail" d="M82 90h40 M82 166h40"/><circle class="solid" cx="168" cy="90" r="5"/><circle class="solid" cx="168" cy="166" r="5"/>'),
'cloud-sync':('Cloud sync','blue','<path d="M79 165a37 37 0 0 1-2-73 51 51 0 0 1 98-7 39 39 0 0 1 3 77"/><path class="detail" d="M104 128a31 31 0 0 1 53-5l9 12 m0-20v20h-20 M152 174a31 31 0 0 1-53-5l-9-12 m0 20v-20h20"/>'),
'search':('Search','blue','<circle cx="113" cy="109" r="49"/><path d="m149 147 43 43"/><path class="detail" d="M88 106q3-22 24-23"/>'),
'bookmark':('Bookmark','rose','<path d="M85 57h86v145l-43-30-43 30Z"/><path class="detail" d="m128 84 7 15 17 3-12 12 2 17-14-8-15 8 3-17-12-12 17-3Z"/>'),
'notification':('Notifications','gold','<path d="M72 171q17-17 17-43V107a39 39 0 0 1 78 0v21q0 26 17 43Z M110 191q18 21 36 0 M128 53v13"/>'),
'history':('History','violet','<path d="M66 102a68 68 0 1 1-1 51 M59 68v39h39"/><path class="detail" d="M128 87v44l29 17"/>'),
'sliders':('Adjust','teal','<path d="M77 58v52 m0 30v58 M128 58v92 m0 30v18 M179 58v22 m0 30v88"/><circle cx="77" cy="125" r="15"/><circle cx="128" cy="165" r="15"/><circle cx="179" cy="95" r="15"/>'),
'folder':('Folder','gold','<path d="M57 100V72q0-12 12-12h46l16 20h56q12 0 12 12v11 M58 105h143l-20 88H77Z"/><path class="detail" d="M99 134h57 M99 154h37"/>'),
'smart':('Smart','violet','<path d="M122 54q4 53 57 60-53 7-57 60-7-53-60-60 53-7 60-60Z"/><path class="detail" d="M187 151q2 25 27 28-25 3-27 28-3-25-28-28 25-3 28-28Z"/>'),
'star':('Star','gold','<path d="m128 52 23 48 53 8-38 38 9 54-47-25-47 25 9-54-38-38 53-8Z"/>'),
'proxy':('Proxy','blue','<circle cx="128" cy="128" r="63"/><path class="detail" d="M65 128h126 M128 65q-49 63 0 126 M128 65q49 63 0 126 M76 95h104 M76 161h104"/>'),
'ponte':('Ponte bridge','teal','<path d="M49 172h158 M65 168V86 M191 168V86 M65 98q63 85 126 0 M91 126v42 M116 143v25 M141 143v25 M166 126v42"/>'),
'direct':('Direct','teal','<path d="M54 128h144 M155 83l44 45-44 45"/>'),
'reject':('Reject','rose','<circle cx="128" cy="128" r="64"/><path class="detail" d="m84 84 88 88"/>'),
'fallback':('Fallback','gold','<path d="M57 82h111q24 0 24 25t-24 25H88q-24 0-24 25t24 25h108 M174 160l22 22-22 22"/>'),
'balance':('Load balance','teal','<path d="M128 53v136 M72 192h112 M72 86h112 M80 86l-28 58h56Z M176 86l-28 58h56Z"/>'),
'ai':('AI','violet','<rect x="79" y="79" width="98" height="98" rx="23"/><path class="detail" d="M103 62V46 M128 62V46 M153 62V46 M103 210v-16 M128 210v-16 M153 210v-16 M62 103H46 M62 128H46 M62 153H46 M210 103h-16 M210 128h-16 M210 153h-16"/><path d="m128 102 6 20 20 6-20 6-6 20-6-20-20-6 20-6Z"/>'),
'streaming':('Streaming','rose','<rect x="55" y="72" width="146" height="104" rx="20"/><path d="m112 101 39 23-39 23Z"/><path class="detail" d="M95 199h66 M128 177v21"/>'),
'game':('Gaming','violet','<path d="M87 91h82q24 0 33 36l8 40q2 23-18 23-12 0-32-23H96q-20 23-32 23-20 0-18-23l8-40q9-36 33-36Z"/><path class="detail" d="M90 119v30 M75 134h30"/><circle class="solid" cx="161" cy="122" r="6"/><circle class="solid" cx="177" cy="140" r="6"/>'),
'rocket':('Launch','rose','<path d="M108 153q-11-57 82-99 10 94-47 114Z M108 110q-40-2-45 48l42-10 M151 158q2 40-48 45l10-42"/><circle class="detail" cx="156" cy="94" r="14"/><path class="detail" d="m90 175-23 23 M85 158l-22 8 M108 181l-8 24"/>')}
pal={'blue':('#4B83E8','#E8F0FF'),'teal':('#329B8C','#E6F5EE'),'gold':('#C99228','#FFF2D1'),'rose':('#D66A73','#FCECEF'),'violet':('#8B72C9','#F0EBFB')}
base=Path('signal')
for family in ['handdrawn-color','minimal']:
 for idx,(name,(title,color,shape)) in enumerate(icons.items()):
  ink='#23282E'; accent,wash=pal[color]
  if family=='handdrawn-color':
   background=f'<rect x="8" y="8" width="240" height="240" rx="55" fill="url(#paper)"/><path d="M66 86Q128 35 193 82L185 179Q131 216 67 174Z" fill="{wash}" transform="rotate({(idx%3-1)*3} 128 128)"/>'
   styling=f'path,rect,circle{{stroke:{ink};stroke-width:7;stroke-linecap:round;stroke-linejoin:round;fill:none}}.glyph .detail{{stroke:{accent};stroke-width:6}}.glyph .solid{{fill:{accent};stroke:none}}'
   deco=f'<path d="M209 50v12 M203 56h12" stroke="{accent}" stroke-width="3" stroke-linecap="round"/><circle cx="48" cy="203" r="2.5" fill="{accent}"/>'
   content=f'<g transform="rotate({[0,-2,1,-1][idx%4]} 128 128)">{shape}</g>'
  else:
   background='<rect x="8" y="8" width="240" height="240" rx="55" fill="#FAFAF9"/>'
   styling=f'path,rect,circle{{stroke:{ink};stroke-width:7;stroke-linecap:round;stroke-linejoin:round;fill:none}}.glyph .detail{{stroke:{ink};stroke-width:7}}.glyph .solid{{fill:{ink};stroke:none}}'
   deco='';content=shape
  # Scope styles to glyphs: keep background fill attributes intact.
  svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 256 256" role="img" aria-labelledby="title"><title id="title">{title}</title><defs><linearGradient id="paper" x2="0" y2="1"><stop stop-color="#FFFFFF"/><stop offset="1" stop-color="#F1F0EC"/></linearGradient></defs>{background}<g class="glyph"><style>{styling.replace('path,rect,circle','.glyph path,.glyph rect,.glyph circle')}</style>{content}</g>{deco}</svg>'''
  (base/family/'source'/f'{name}.svg').write_text(svg+'\n')
 entries=[{'name':v[0],'url':f'https://raw.githubusercontent.com/lucking7/H.F./codex/signal-icon-families/signal/{family}/128/{k}.png'} for k,v in icons.items()]
 index={'name':"LUCK's "+('手绘彩色 UI' if family=='handdrawn-color' else '极简 UI'),'description':'Original scalable utility icons. 128px RGBA assets for Surge policy groups.','icons':entries}
 Path('UI-'+('Handdrawn' if family=='handdrawn-color' else 'Minimal')+'.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
Path('signal/icon-catalog.json').write_text(json.dumps({k:{'name':v[0],'color':v[1]} for k,v in icons.items()},ensure_ascii=False,indent=2)+'\n')
