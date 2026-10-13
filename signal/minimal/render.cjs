// Rebuild this family from its SVGs. npm install sharp first.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const root = __dirname;
(async () => {
  for (const f of fs.readdirSync(path.join(root, 'source')).filter(f => f.endsWith('.svg'))) {
    for (const size of [128, 512]) await sharp(path.join(root, 'source', f)).resize(size, size).png().toFile(path.join(root, String(size), f.replace('.svg', '.png')));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
