const fs=require('fs'),path=require('path');
const sharp=require(process.env.SHARP_MODULE||'sharp');
(async()=>{for(const family of ['handdrawn-color','minimal']){for(const size of [128,512]){const dir=`signal/${family}/${size}`;fs.mkdirSync(dir,{recursive:true});for(const f of fs.readdirSync(`signal/${family}/source`)){await sharp(`signal/${family}/source/${f}`).resize(size,size).png().toFile(path.join(dir,f.replace('.svg','.png')))}}}console.log('Rendered 96 RGBA PNGs from 48 original SVGs');})();
