const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '../..');
const icons = JSON.parse(fs.readFileSync(path.join(root, 'UI-Handdrawn-Ink.json'))).icons;
(async () => {
  for (const [filename, size] of [['preview.png', 180], ['preview-small.png', 64]]) {
    const gap = 26, width = 6 * (size + gap) + gap, height = 4 * (size + 55) + gap;
    const layers = [];
    let labels = '';
    for (const [index, icon] of icons.entries()) {
      const input = path.join(root, icon.url.split('/main/')[1]);
      const left = gap + index % 6 * (size + gap), top = 20 + Math.floor(index / 6) * (size + 55);
      layers.push({ input: await sharp(input).resize(size, size).toBuffer(), left, top });
      labels += `<text x="${left + size / 2}" y="${top + size + 23}" text-anchor="middle">${icon.name}</text>`;
    }
    layers.push({ input: Buffer.from(`<svg width="${width}" height="${height}"><style>text{font:${size === 64 ? 11 : 15}px sans-serif;fill:#364252}</style>${labels}</svg>`), left: 0, top: 0 });
    await sharp({ create: { width, height, channels: 4, background: '#f2f3f5' } }).composite(layers).png().toFile(path.join(__dirname, filename));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
