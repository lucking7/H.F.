# Flag collection

[Flags.json](../Flags.json) contains the user-selected flags and two preserved historical artworks. [selection.json](selection.json) records the selections and refinements.

## Style

Redrawn flags use a 1024 × 772 transparent canvas, a 1008 × 756 card at (8, 8), and 64 px corners. Proportions and palettes are decorative rather than official specifications. The base coral and indigo palette follows the original USA-1 design.

Japan, Singapore and Korea use the selected B treatment: continuous white shading, a subtle light rim and a lower edge. Singapore's crescent and stars use a separate local white gradient.

Germany uses a separate gradient inside each stripe, avoiding a muddy yellow band caused by global shading. Its endpoints are charcoal `#424242` → `#171717`, coral `#FF6454` → `#DC3929`, and gold `#FFE06A` → `#F1BF32`.

Belgium uses the same brighter gold endpoints as Germany. Ireland and Italy have lighter green shadows; Ireland also has a brighter orange. The Netherlands uses a local indigo gradient inside its blue stripe (`#3659A8` → `#173681`) to avoid a nearly flat dark base. Other selected palettes remain unchanged.

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
