#!/usr/bin/env python3
"""Write a separate profile, changing only icon-url in known policy groups."""
import argparse,json,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);p.add_argument('--family',choices=['handdrawn-color','minimal'],required=True);args=p.parse_args()
if args.source.resolve()==args.output.resolve():p.error('Use a separate output path; back up before installing it.')
mapping=json.loads(Path(__file__).with_name('icon-map.json').read_text());section='';out=[];changed=[]
for line in args.source.read_text().splitlines(keepends=True):
 if line.lstrip().startswith('['):section=line.strip()
 if section=='[Proxy Group]' and '=' in line and not line.lstrip().startswith(('#',';')):
  name=line.split('=',1)[0].strip();url=None
  if name in mapping['groups']:url=f"{mapping['asset_base']}/{args.family}/128/{mapping['groups'][name]}.png"
  elif name in mapping['flags']:url=f"{mapping['flag_base']}/{mapping['flags'][name]}.png"
  if url:
   if re.search(r'(?<![\w-])icon-url\s*=',line):line=re.sub(r'(?<![\w-])icon-url\s*=\s*[^,\r\n]+','icon-url='+url,line)
   else:line=line.rstrip('\r\n')+', icon-url='+url+'\n'
   changed.append(name)
 out.append(line)
args.output.write_text(''.join(out));print(f'{len(changed)} policy-group icon mappings written; no other fields changed.')
