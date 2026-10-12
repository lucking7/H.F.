---
name: Prism Strategy Icons
description: A 24-icon strategy-group set with layered geometry and a restrained static glass treatment.
colors:
  porcelain-top: "#FFFFFF"
  porcelain-middle: "#F4F6FA"
  porcelain-bottom: "#E0E5ED"
  layer-background: "#F5F7FB"
rounded:
  static-enclosure: "53/256 canvas units"
---

# Design System: Prism Strategy Icons

## Overview

**Creative North Star: "Porcelain Prism"**

The set translates proxy strategy groups into compact, readable symbols. A pale porcelain enclosure keeps the collection coherent, while one two-stop hue family gives each strategy a distinct identity. The artwork is newly authored and uses Apple Icon Composer and App icon guidance as references for layered composition, not as proof of native output.

The delivered assets are 24 composite SVGs, 24 static 1024 × 1024 PNGs, 24 static 144 × 144 PNGs, and unmasked layer SVGs. No `.icon` project, dynamic refraction, native dark or monochrome appearance, Icon Composer import test, or device validation is included.

## Colors

The enclosure moves from Porcelain Top through Porcelain Middle to Porcelain Bottom. Each symbol uses the following top-to-bottom pair; translucency and highlights may introduce lighter derived tones in composite output.

| Icon | Top | Bottom |
| --- | --- | --- |
| Star | `#FFD65B` | `#ED8B16` |
| Smart | `#52E6DD` | `#008FAB` |
| Auto | `#6CBBFF` | `#2359E9` |
| Select | `#B9A3FF` | `#6D42D7` |
| Fallback | `#FFB96D` | `#E56727` |
| Load Balance | `#6DDEBE` | `#138D75` |
| Direct | `#75DBA0` | `#20924D` |
| Proxy | `#75B1FF` | `#3258CB` |
| Global | `#58D7EF` | `#087EA8` |
| Rules | `#ADB4FF` | `#5962C7` |
| Reject | `#FF8D94` | `#D73B4C` |
| DNS | `#7FDCDD` | `#208D98` |
| Speed | `#FFC267` | `#E58816` |
| Privacy | `#82B9FF` | `#3A5CCA` |
| Stream | `#FF9A7A` | `#E75235` |
| AI | `#C79CFF` | `#8245CA` |
| Search | `#6AC8FF` | `#247CB9` |
| Social | `#FFA2CC` | `#CB4585` |
| Game | `#AE9AFF` | `#7050C8` |
| Work | `#83C2DD` | `#3A799D` |
| Download | `#6ACFDB` | `#178B9B` |
| Update | `#91CEA3` | `#388656` |
| Cloud | `#8DCBFF` | `#3C85C8` |
| Final | `#A6B8C9` | `#546B84` |

**The Silhouette First Rule.** Color separates categories, but every icon must remain identifiable by geometry at 144px.

## Layout

All artwork uses a square 1024 × 1024 file canvas. Back, front, and accent layer SVGs share a 256-unit viewBox and retain their geometry at 100%. Composite SVGs group those artwork layers and apply a centered 87% scale (`translate(128 128) scale(.87) translate(-128 -128)`); the opaque background remains full canvas. Raw artwork imported at 100% is therefore about 14.9% larger than the composite glyph. Apply the same centered 87% group scale when matching the static output.

## Elevation & Depth

Composite SVGs and PNGs simulate glass statically with a colored rear layer, translucent or pale foreground, a crisp gradient rim, top illumination, and two soft drop-shadow levels. These effects are baked into the composite representation. The files in `layers/` contain no lighting, shadow, rounded mask, or dynamic material behavior.

**The Native Material Rule.** When building a real Icon Composer project, import the unmasked layers and recreate material, masking, and depth in Icon Composer rather than stacking the pre-rendered composite.

## Shapes

The static enclosure is a rounded square spanning 240 × 240 units from `(8, 8)` on the 256-unit canvas, with a 53-unit corner radius and a one-unit rim. Symbols use filled geometry with rounded terminals where the subject permits. They contain no letters or emoji.

## Components

The shared layer order is `background`, `back`, `front`, then optional `accent`:

- **Background:** opaque `#F5F7FB`, full canvas, never scaled with the glyph.
- **Back:** solid color-bearing depth silhouette.
- **Front:** main readable symbol, intended for translucency or pale material treatment.
- **Accent:** optional highlight or semantic detail above the foreground.

The 24 names are Star, Smart, Auto, Select, Fallback, Load Balance, Direct, Proxy, Global, Rules, Reject, DNS, Speed, Privacy, Stream, AI, Search, Social, Game, Work, Download, Update, Cloud, and Final.

## Do's and Don'ts

### Do:

- **Do** preserve each icon's silhouette, layer order, shared center, and paired hue family.
- **Do** evaluate both 1024px and 144px static exports after geometry changes.
- **Do** use the layer SVGs as the starting point for a future native Icon Composer project.

### Don't:

- **Don't** describe the static gradients and shadows as dynamic Liquid Glass or real-time refraction.
- **Don't** treat the light and dark contact sheets as native appearance variants.
- **Don't** claim Icon Composer or device acceptance until those checks have actually been run.

Official references: [Apple Icon Composer](https://developer.apple.com/icon-composer/) and [Apple Human Interface Guidelines: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/), consulted 2026-10-12.
