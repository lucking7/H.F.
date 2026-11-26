# Hchi's Icon Repository

## Collections

The [combined subscription](https://raw.githubusercontent.com/lucking7/H.F./main/All.json) covers apps, flags, regional artwork, UI, and network policy groups. [All.json](All.json) lists each image path once and keeps different sizes and styles. REX icons are available through the dedicated REX subscriptions below.

| Collection | Indexes | Artwork and sources |
| --- | --- | --- |
| Apps and brands | [All apps](Apps.json) · [144px](Apps144px.json) | [App and brand artwork](logo/) · [AI glass icons and macOS downloads](logo/ai-glass/README.md) |
| Flags | [Rectangular](Flags.json) · [macOS 1024px](Flags-macOS.json) · [macOS 144px](Flags-macOS144px.json) | [Flag previews, Icon Composer projects and ICNS downloads](flags/README.md) |
| Regions and organizations | Symbols [1024px](Region-Symbols.json) · [144px](Region-Symbols144px.json) · Colored letters [1024px](Region-Letters-Color.json) · [144px](Region-Letters-Color144px.json) | [Artwork, palette and sources](flags/regions/README.md) |
| UI | [Combined UI](UI.json) · [Ink](UI-Handdrawn-Ink.json) | The combined index includes 54 images. The [ink collection](signal/ink/README.md) includes 10 originals and 14 new drawings. |
| Network policy groups | [1024px](Routing-Policy.json) · [144px](Routing-Policy144px.json) | [Proxy, Star, Smart, Ponte, and AI artwork](signal/routing-policy/README.md) |
| REX | [All 138 entries](REX.json) · [10 white platform badges](REX-Platforms.json) · [26 runtime logos](REX-Runtime.json) | [Collection guide](rex-icons/1.0.0/README.md) and [manifest of 181 image files](rex-icons/1.0.0/manifest.json), including original variants. |

## Local review

Run `python3 -m http.server 8741 --bind 127.0.0.1` from the repository root and open [the local review page](http://127.0.0.1:8741/review/). It opens on the AI glass icons. Use the collection menu to browse the full library or open the [network policy group gallery](http://127.0.0.1:8741/review/?collection=Routing-Policy.json) directly. Review marks are saved in the current browser and can be exported as JSON.

The [combined subscription view](http://127.0.0.1:8741/review/?collection=all) shows the names in `All.json`. Search also accepts names from the individual indexes.

Four legacy files have a `.png` extension and contain Photoshop documents. The review page displays their merged images from `review/previews/` and offers the original PSDs for download.

## Rebuilding collections

Follow the [ink collection guide](signal/ink/README.md) to render its images and update its index. Then run `python3 tools/update-ui-index.py` from the repository root to add new ink images to the combined UI index.

After changing a collection index, run `python3 tools/update-all-index.py` to refresh `All.json`. The generator checks that every URL resolves to an image file in the working tree before replacing the combined index.

---

> [!CAUTION]
> ACCESS TO THIS REPOSITORY IS RESTRICTED. UNAUTHORIZED DISTRIBUTION OR MONETIZATION WITHIN THE BORDERS OF THE PEOPLE'S REPUBLIC OF CHINA IS STRICTLY PROHIBITED AND MAY RESULT IN IMMEDIATE [REDACTED].

> [!IMPORTANT]
> ALL ICONS CONTAINED HEREIN ARE COLLECTED FROM VARIOUS NETWORK SOURCES. COPYRIGHT BELONGS TO THEIR RESPECTIVE CREATORS. IN CASE OF INFRINGEMENT, CONTACT SITE DIRECTOR [REDACTED] FOR IMMEDIATE REMOVAL.

> [!IMPORTANT]
> REPRODUCTION OF THIS MATERIAL REQUIRES PRESERVATION OF ORIGINAL ATTRIBUTION AND ADHERENCE TO THE CC BY-NC-SA 4.0 LICENSE AS DETAILED IN DOCUMENT [https://github.com/lucking7/H.F.]. FAILURE TO COMPLY MAY RESULT IN [DATA EXPUNGED].
