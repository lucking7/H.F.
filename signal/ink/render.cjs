const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const root = __dirname;
(async () => {
  for (const name of fs.readdirSync(path.join(root, 'source')).filter(n => n.endsWith('.svg'))) {
    for (const size of [128, 1024]) {
      await sharp(path.join(root, 'source', name)).resize(size, size).png().toFile(path.join(root, String(size), name.replace('.svg', '.png')));
    }
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
