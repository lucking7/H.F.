// Run from the repository root after rendering the PNGs.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
const icons = JSON.parse(fs.readFileSync(path.join(root, 'manifest.json'))).icons;
(async () => {
  for (const [name, size, gap, background] of [
    ['preview-light.png', 180, 35, '#edf0f5'],
    ['preview-dark.png', 180, 35, '#1a202c'],
    ['preview-small.png', 48, 36, '#edf0f5'],
    ['preview-color.png', 180, 35, '#edf0f5'],
    ['preview-color-small.png', 48, 36, '#edf0f5'],
  ]) {
    const width = 6 * (size + gap) + gap;
    const height = 4 * (size + gap + 25) + gap;
    const layers = [];
    let labels = '';
    for (const [index, icon] of icons.entries()) {
      const left = gap + (index % 6) * (size + gap);
      const top = gap + Math.floor(index / 6) * (size + gap + 25);
      layers.push({ input: await sharp(path.join(root, name.includes('color') ? 'color' : 'png', icon.slug + '.png')).resize(size, size).toBuffer(), left, top });
      labels += `<text x="${left + size / 2}" y="${top + size + 22}" text-anchor="middle">${icon.name}</text>`;
    }
    const color = name === 'preview-dark.png' ? '#edf0f5' : '#364455';
    layers.push({ input: Buffer.from(`<svg width="${width}" height="${height}"><style>text{font:${size === 48 ? 11 : 16}px sans-serif;fill:${color}}</style>${labels}</svg>`), left: 0, top: 0 });
    await sharp({ create: { width, height, channels: 4, background } }).composite(layers).png().toFile(path.join(root, name));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
