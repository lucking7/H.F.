# Flag collection

[Flags.json](../Flags.json) is the single index. Each country, region or international flag has one version. Duplicate variants, test exports, Photoshop drafts and unrelated organizational artwork have been removed; their original files remain in Git history. The former `FlagsRecommended.json` has been retired.

## Style

All cards use a 1024 × 772 RGBA canvas, with a 1008 × 756 rounded rectangle at (8, 8), a 64 px corner radius and transparent corners. There are no external shadows or borders. The decorative 4:3 cards do not reproduce each flag's official aspect ratio or official colors.

The colors and vertical shading follow the original `USA00001.png`:

| Material | Top | Bottom |
| --- | --- | --- |
| Coral red | `#FF6454` | `#C52A1A` |
| Indigo blue | `#425FAD` | `#072472` |
| White | `#FFFFFF` | `#DEDEDE` |

Red and blue reach their final shades at 82% of the card height. White stays white through the upper 34%, then shades to gray at 82%. Other colors use the same restrained vertical treatment while preserving the flag's recognizable hue. The UN retains its light blue.

`USA00001.png` has been redrawn in the preferred original palette, with 50 five-point stars in nine alternating rows of six and five, and 13 stripes. The old drawing's stripe-count error and edge artifact are removed. Versions 2, 3 and 4 are no longer part of the collection.

## Sources

Every PNG has an editable counterpart in [source/](source/). Except for the explicitly drawn US stars and stripes, geometry is adapted from [lipis/flag-icons](https://github.com/lipis/flag-icons) at commit `086f7e97d657358203916dbe84f61c2bccaa81eb`. Its MIT notice is preserved in [LICENSE.flag-icons](source/LICENSE.flag-icons). Palette, gradients, card shape and exports were redrawn for this repository.

With `sharp` installed, an SVG can be exported without changing its canvas:

```sh
node -e "require('sharp')(process.argv[1]).png().toFile(process.argv[2])" flags/source/NLD00001.svg flags/rectangle/NLD00001.png
```
