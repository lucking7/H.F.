// npm install sharp, then node strategy/scripts/render.cjs from the repository root.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
function addOrigin(file, slug) {
  const origin = `Origin: original deterministic vector artwork in strategy/source/${slug}.svg, authored by Codex for the user; rasterized with sharp. No generative-image model used. Reference: https://developer.apple.com/icon-composer/`;
  const data = Buffer.from('impeccable:prompt\0' + origin, 'utf8');
  const type = Buffer.from('tEXt');
  let crc = 0xffffffff;
  for (const byte of Buffer.concat([type, data])) {
    crc ^= byte;
    for (let bit = 0; bit < 8; bit++) crc = (crc >>> 1) ^ ((crc & 1) ? 0xedb88320 : 0);
  }
  const length = Buffer.alloc(4); length.writeUInt32BE(data.length);
  const checksum = Buffer.alloc(4); checksum.writeUInt32BE((crc ^ 0xffffffff) >>> 0);
  const png = fs.readFileSync(file);
  fs.writeFileSync(file, Buffer.concat([png.subarray(0, -12), length, type, data, checksum, png.subarray(-12)]));
}
const dir = path.resolve(__dirname, '..');
(async () => {
  for (const filename of fs.readdirSync(path.join(dir, 'source')).filter(name => name.endsWith('.svg'))) {
    const source = path.join(dir, 'source', filename);
    const png = filename.replace(/\.svg$/, '.png');
    await sharp(source).png().toFile(path.join(dir, 'png', png));
    await sharp(source).resize(144, 144).png().toFile(path.join(dir, '144px', png));
    addOrigin(path.join(dir, 'png', png), filename.replace(/\.svg$/, ''));
    addOrigin(path.join(dir, '144px', png), filename.replace(/\.svg$/, ''));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
