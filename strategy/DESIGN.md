# Relief visual system · v2

## User direction

Large, simple matte relief rather than small multicolor objects sitting on a pale tile. References are the supplied red tile / white symbol image and https://macosicons.com/?icon=DAZC158WJJ (CapCut Golden Gate Dark by xdan).

## Geometry

1024px square export; viewBox 0 0 256 256. Static enclosure: x/y 8, size 240, corner radius 54. Glyph envelope: approximately 186 units, centered optically at (128,127). Each glyph has its own bounds so narrow cursors and wide arrows carry similar visual weight. Star is a five-point star; Smart is a four-point spark; AI is a chip with a cutout spark. Update adds a downward arrow inside the cycle.

## Material

Porcelain background #FFFFFF to #ECEEF1; graphite symbol #17191C to #707276; soft shadow offset 3.6 units / blur 2.6 / opacity .18. Color appearance uses the subject palette bottom value from manifest.json, ivory symbol #FFFFFF to #EBECED, and a short tinted shadow. A gentle lower fade integrates the symbol into the backing. The material is a static simulation, not dynamic refraction.

## Sources

Composite SVGs carry static lighting and an enclosure. Raw background/glyph layers have no filters, gradients or corner masks; SVG masks encode negative spaces only. Raw layers carry the final symbol size, so do not apply the old 87% Prism scale. No native `.icon` file, native dark/mono mode or import/device verification is claimed.

## Scope

24 identities listed in manifest.json and two color appearances, each exported at 1024px and 144px. Existing App/UI and other flag collections are independent. The previous Prism version remains in Git history.
