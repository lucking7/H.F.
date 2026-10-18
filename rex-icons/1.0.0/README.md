# REX 1.0.0 build 10 icons

These resources form an independent REX collection. Existing Flags, Apps and UI collections remain separate.

| Consumer index | Entries | Contents |
| --- | ---: | --- |
| [REX.json](../../REX.json) | 138 | All indexed REX resources, including size and appearance variants |
| [REX-Platforms.json](../../REX-Platforms.json) | 10 | Local white transparent platform badges |
| [REX-Runtime.json](../../REX-Runtime.json) | 26 | Runtime logos, 14 colored and 12 monochrome |

Consumer indexes use `{name, description, icons: [{name, url}]}`. Names are stable unique IDs. Platform and runtime indexes are subsets of the full index.

## Sources and originals

- 112 entries were extracted from the REX 1.0.0 build 10 application resources. These include 10 platform badges, 31 media badges, 68 catalog renditions, two app icon entries and one decoration. Entries include size/appearance variants and do not represent 112 distinct brands.
- 26 additional platform, studio and network logos came from TMDB URLs referenced by the same application's runtime. [runtime-logos.json](runtime-logos.json) records each source URL, original color classification, dimensions and SHA-256. Apple TV+ is black in this set. Images have not been recolored.
- [icons.json](icons.json) retains category, dimensions, appearance/scale where available, SHA-256 and original asset links. [platforms.json](platforms.json) provides detailed metadata for the white badges.
- [manifest.json](manifest.json) lists all 181 image files, byte sizes and SHA-256 hashes. The count exceeds 138 because the original 41 WebP badges and two original app PNGs are retained alongside standard PNG versions. The two original app PNGs use Apple’s CgBI encoding and are retained for provenance; normal image clients should use the standard PNG conversions referenced by the consumer indexes. No CAR archives, binaries, private configuration or extraction tools are included.

Platform white badges and runtime colored/monochrome logos coexist; one does not replace the other. All logos and trademarks remain the property of their respective owners. Extraction and inclusion do not grant additional rights.
