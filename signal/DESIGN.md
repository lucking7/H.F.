# Two Signal icon families

Two original utility icon families, each with 24 functional symbols and identical names. `handdrawn-color` uses warm paper, organic color washes, a slight optical tilt and colored ink accents. `minimal` uses a neutral surface, a controlled stroke weight and no decorative marks. The minimal family follows broad principles of reduction, negative space and functional recognition; it does not reproduce ChatGPT, Grok or another product's marks. The Egolite reference remains unconfirmed.

Sources: editable SVG at `signal/<family>/source/<name>.svg`. PNG exports: 512px for reuse and 128px for Surge. Corners have real transparency. SVGs are original deterministic drawings, not AI-generated raster crops. The earlier imagegen concept board informed the hand-drawn family; these are independent, editable implementations.

## Surge mapping

| Group | Symbol | Color |
| --- | --- | --- |
| Proxy | proxy / globe | Blue |
| Star | star | Gold |
| Smart | smart / paired sparkles | Violet |
| Ponte | ponte / bridge | Teal |
| 🇺🇸 🇯🇵 🏴‍☠️ 🇭🇰 🇸🇬 🇳🇱 🇺🇳 | Existing country or organization flag | Existing palette |

🇳🇱 maps to the Netherlands flag, not the EU flag. 🇺🇳 maps to the current `UN.png`. No group names, policy membership, route rules, credentials, or node definitions belong in this public package.

Additional symbols cover credentials, protection, linking, routing, server, cloud sync, search, bookmark, notifications, history, sliders, folder, direct, reject, fallback, balancing, AI, streaming, gaming and launch. At small sizes, prefer the dedicated 128px export; original sources remain editable.

## Rebuild

Install `sharp` in your Node environment, then run from the repository root:

```sh
python3 tools/build-signal-icons.py
node tools/render-signal-icons.cjs
node tools/preview-signal-icons.cjs
```

`SHARP_MODULE` can point to an already installed module. No existing App/UI collection or flag is replaced. Indexes are `UI-Handdrawn.json` and `UI-Minimal.json`.
