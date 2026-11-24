# AI glass icons

Four new designs accompany the two supplied Claude Code icons. The PNG exports are listed in the [app index](../../Apps.json) and the [144px index](../../Apps144px.json).

![Six app icons with their names and finishes](preview.png)

| Icon | macOS | PNG | Editable artwork |
| --- | --- | --- | --- |
| Claude · Amber Glass | [ICNS](icns/claude.icns) | [1024px](png/claude.png) · [144px](144px/claude.png) | [SVG](source/claude.svg) |
| OpenAI · Nacre Glass | [ICNS](icns/openai.icns) | [1024px](png/openai.png) · [144px](144px/openai.png) | [SVG](source/openai.svg) |
| Codex · Cobalt Glass | [ICNS](icns/codex.icns) | [1024px](png/codex.png) · [144px](144px/codex.png) | [SVG](source/codex.svg) |
| AI Silicon | [ICNS](icns/ai-silicon.icns) | [1024px](png/ai-silicon.png) · [144px](144px/ai-silicon.png) | [Python renderer](source/ai-silicon.py) |
| Claude Code Liquid Glass Light | [Original ICNS](icns/claude-code-light.icns) | [1024px](png/claude-code-light.png) · [144px](144px/claude-code-light.png) | Supplied artwork |
| Claude Code Liquid Glass White | [Original ICNS](icns/claude-code-white.icns) | [1024px](png/claude-code-white.png) · [144px](144px/claude-code-white.png) | Supplied artwork |

## Artwork

The three brand icons share a glass edge that catches color in opposite corners. Claude pairs a copper starburst with a warm porcelain tile. OpenAI uses a mother-of-pearl knot over smoked graphite. The Codex terminal prompt sits inside a raised cobalt cloud. The brand silhouettes come from the installed Claude and Codex applications. The tiles, optical finishes and compositions were drawn for this collection.

AI Silicon depicts an exposed accelerator package with a patterned compute die, four high-bandwidth memory stacks and gold traces. Its geometry and material lighting are procedurally drawn. From the repository root, run `python3 logo/ai-glass/source/ai-silicon.py` with NumPy and Pillow to regenerate the 1024px PNG. Use `rsvg-convert logo/ai-glass/source/claude.svg -o logo/ai-glass/png/claude.png` to render the Claude design, and substitute the other SVG filenames for OpenAI and Codex.

The two original ICNS files retain the bytes supplied as `Claude_Code_liquid_glass_Light_b3Yp5kFVQA-19ed537871.icns` and `Claude_Code_liquid_glass_white_BTBvaXMiCZ-0473a737d2.icns`. Their 1024px PNGs come directly from the embedded full-size images, and their 144px versions use the embedded 256px images.
