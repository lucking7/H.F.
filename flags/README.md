# Flag collection

[Flags.json](../Flags.json) contains the user-selected flags and two preserved historical artworks. [selection.json](selection.json) records the selections and refinements.

## Style

Redrawn flags use a 1024 × 772 transparent canvas, a 1008 × 756 card at (8, 8), and 64 px corners. Proportions and palettes are decorative rather than official specifications. The base coral and indigo palette follows the original USA-1 design.

All 16 redrawn flags share one card-space light model. Every material uses the same continuous curve from the top to the bottom, with stops at 0%, 18%, 55%, 86% and 100%. Paints retain their inverse geometry transforms so differently positioned or rotated shapes receive light in the same card coordinates. No stripe restarts the light gradient.

A broad, low-opacity highlight falls from the upper left across the whole flag. A rounded inner bevel and thin rim add visible edge thickness, with a light top and shaded bottom. These overlays cover the assembled flag rather than individual stripes or symbols. The 1024 × 772 canvas and outer card geometry remain unchanged; no external drop shadow is added.

The white material ends at `#CDD2D9`, coral at `#CF3222`, and indigo at `#163774`. Germany and Belgium retain the brighter gold; Ireland and Italy retain their refined green palettes. The UN keeps its cyan-to-blue character. The earlier stripe-local gradients and one-sided lower edge have been replaced.

## United Nations and institution artwork

- `UN.png`: refined vector redraw of the United Nations flag, with saturated cyan-to-blue shading (`#64CEFF` → `#00619E`).
- `UN-classic.png`: the original `UNO00003.png`, preserved byte-for-byte from commit `50dd75c`.
- `INSTITUTION.png`: the original red building/pediment icon named `UNO00001.png`, preserved byte-for-byte from commit `50dd75c`. Its neutral name describes the image without attributing it to the United Nations or a particular institution.

The two historical raster images retain their original canvas, edges and colors. They have no editable SVG counterpart; all redrawn flags have sources in [source/](source/). Superseded files remain recoverable through Git history. Apps and UI icons are maintained independently.

## Sources and export

Except for the explicitly drawn US stars and stripes, vector geometry is adapted from [lipis/flag-icons](https://github.com/lipis/flag-icons) at commit `086f7e97d657358203916dbe84f61c2bccaa81eb`. Its MIT notice is preserved in [LICENSE.flag-icons](source/LICENSE.flag-icons).

With `sharp` installed:

```sh
node -e "require('sharp')(process.argv[1]).png().toFile(process.argv[2])" flags/source/NLD00001.svg flags/rectangle/NLD00001.png
```
