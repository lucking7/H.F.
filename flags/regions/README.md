# Regions and organizations

Two macOS 26 icon sets for regional and organization labels. The shallow-relief collection includes nine symbols and ten colored letter icons. The 144 px PNGs have 7 px of transparent padding on each side. Use the 144 px catalogs for compact lists in Surge.

| Set | Subscriptions | Artwork and editable source |
| --- | --- | --- |
| Symbols | [1024 px](../../Region-Symbols.json) · [144 px](../../Region-Symbols144px.json) | [1024 px PNG](symbols/png/) · [144 px PNG](symbols/144px/) · [Icon Composer and SVG](symbols/source/) |
| Colored letters | [1024 px](../../Region-Letters-Color.json) · [144 px](../../Region-Letters-Color144px.json) | [1024 px PNG](letters/png/) · [144 px PNG](letters/144px/) · [Icon Composer and SVG](letters/source/) · [Palette](letters/palette.json) |

| Code | Region or organization | Symbol |
| --- | --- | --- |
| US | United States | Stars-and-stripes shield |
| JP | Japan | Mount Fuji and the red sun |
| KR | South Korea | Red-and-blue taegeuk |
| SG | Singapore | Supertrees |
| NL | Netherlands | Windmill |
| DE | Germany | Brandenburg Gate |
| UN | United Nations | Peacekeeper's blue helmet |
| TW | Taiwan | Main-island coastline |
| EU | European Union | Ballot box |
| HK | Hong Kong | Letters only |

## Sources

The Taiwan coastline uses county boundaries from the National Land Surveying and Mapping Center, Ministry of the Interior (2017), *直轄市、縣市界線 (TWD97 經緯度)*, release `COUNTY_MOI_1060525`. The data are available under the Open Government Data License, version 1.0, for use in accordance with its terms. [Official dataset](https://data.gov.tw/dataset/7442) · [License](https://data.gov.tw/license)

The outline combines the county polygons from Taiwan.TopoJSON, keeps the main island's exterior, and simplifies it from 521 vertices to 33. [Pinned TopoJSON](https://github.com/jason2506/Taiwan.TopoJSON/blob/649946d37f84b1591fe353ddab74858dc8427aad/topojson/counties.json) · [Conversion configuration](https://github.com/jason2506/Taiwan.TopoJSON/blob/71b944c4c2237945ac95a40dbd3a5ea8ace61bf6/Makefile)

The EU ballot box is an original vector drawing based on European Parliament election photographs by Marc Dossmann. [Casting a ballot](https://multimedia.europarl.europa.eu/en/photo/ballot-box_20131121_Ballot_Box_041) · [Marking a ballot](https://multimedia.europarl.europa.eu/en/photo/ballot-box_20131121_Ballot_Box_064)
