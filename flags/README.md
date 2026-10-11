# Flag style

Use [FlagsRecommended.json](../FlagsRecommended.json) for the default selection. [Flags.json](../Flags.json) retains all historical variants and their existing URLs.

The recommended style follows the existing ISO3 family: a 1024 × 772 RGBA canvas with a 1008 × 756 card at (8, 8), approximately 64 px corner radius, transparent corners, and subtle vertical shading. There is no external shadow or border. This is a decorative 4:3 icon format, not the official aspect ratio of each national flag.

New national assets use ISO 3166 alpha-3 names. Netherlands is `NLD00001.png`. New cards include Netherlands, Germany, France, Italy, Ireland and Belgium. The editable SVGs are in [source/](source/); their dimensions match the PNG exports. The SVG shading adds up to 12% white at the top and 12% black at the bottom.

## United States

Use `USA00004.png` by default. It contains 50 five-point stars in nine alternating rows of six and five, and 13 alternating stripes. Its card geometry matches the recommended family.

Of the old versions, `USA00001.png` is the better visual reference, but it has only 11 stripes and a small dark artifact near the upper-left edge. `USA00003.png` has 13 stripes but only 28 stars. Both remain available for existing consumers; neither is the recommended US flag.

## Sources and compatibility

The new SVG artwork is drawn for this repository. European base palettes follow the [flag-icons SVG collection](https://github.com/lipis/flag-icons/tree/main/flags/4x3). Shading changes the displayed colors, so these assets are intended as UI icons.

Files with a `.png` extension must contain actual PNG data. Historical files that contained Photoshop data have been re-encoded as PNG at the same paths, preserving the decoded RGBA pixels. Their original bytes remain recoverable from Git history.

To export an SVG with sharp installed, run:

```sh
node -e "require('sharp')(process.argv[1]).png().toFile(process.argv[2])" flags/source/NLD00001.svg flags/rectangle/NLD00001.png
```
