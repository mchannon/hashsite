#!/usr/bin/env python3
from pathlib import Path
import re
import sys

readme = Path("README.md")
backup = Path("README.before-hashsite-menu.bak.md")

MENU = '<!-- HASHSITE_MENU_BEGIN -->\n\n# Hashsite\n\n![Hashsite banner](img/hashsitebanner.png)\n\n**Open geocoding. Short letters and numbers for real-world places. Offline-capable. No API key. No rent.**\n\nHashsite encodes real-world locations as compact, human-shareable alphadecimal strings.\n\nA Hashsite can be short enough to text, print, speak, write on a sticky note, put in a QR code, or paste into another system:\n\n```text\n#7BA2CSoDZ\n#7B6.63IH.XB8\n#7BA2CSoDZ^2\n```\n\nThe map app is the interface.  \nThe code is the durable object.\n\n## Start here\n\n| Topic | Page |\n|---|---|\n| 1. What Hashsite is | [`docs/01-WHAT-IS-A-HASHSITE.md`](docs/01-WHAT-IS-A-HASHSITE.md) |\n| 2. Code format, alphabet, precision, and rubric | [`docs/02-CODES-AND-RUBRIC.md`](docs/02-CODES-AND-RUBRIC.md) |\n| 3. Grid and encoding model | [`docs/03-GRID-AND-ENCODING.md`](docs/03-GRID-AND-ENCODING.md) |\n| 4. Altitude / 3D locations | [`docs/04-ALTITUDE.md`](docs/04-ALTITUDE.md) |\n| 5. Dots and readability checks | [`docs/05-DOTS-AND-READABILITY.md`](docs/05-DOTS-AND-READABILITY.md) |\n| 6. Hashpaths in the Hashsite library | [`docs/06-HASHPATHS-IN-HASHSITE.md`](docs/06-HASHPATHS-IN-HASHSITE.md) |\n| 7. CLI reference | [`docs/07-CLI-REFERENCE.md`](docs/07-CLI-REFERENCE.md) |\n| 8. Library API | [`docs/08-LIBRARY-API.md`](docs/08-LIBRARY-API.md) |\n| 9. Coordinate import and interoperability | [`docs/09-COORDINATE-IMPORT.md`](docs/09-COORDINATE-IMPORT.md) |\n| 10. Web app behavior | [`docs/10-WEB-APP.md`](docs/10-WEB-APP.md) |\n| 11. Design principles | [`docs/11-DESIGN-PRINCIPLES.md`](docs/11-DESIGN-PRINCIPLES.md) |\n| 12. Roadmap | [`docs/12-ROADMAP.md`](docs/12-ROADMAP.md) |\n| 13. Companion product: Hashpath | [`docs/13-COMPANION-HASHPATH.md`](docs/13-COMPANION-HASHPATH.md) |\n| Preserved original README material | [below](#preserved-original-readme-material) |\n\n## One-minute version\n\nHashsite is a coordinate format, library, CLI, and web app for turning real-world locations into short alphadecimal codes.\n\nIt is meant to be:\n\n- compact\n- offline-capable\n- hierarchical\n- human-handleable\n- machine-decodable\n- 2D and 3D aware\n- open to implement\n- useful without renting an API\n\n## Examples\n\n| Code | Meaning |\n|---|---|\n| `#7BA2` | Potter County, TX area — coarse, 4-character Hashsite |\n| `#7BA2CSoDZ` | Cadillac Ranch / Amarillo-area point — person-scale precision |\n| `#7BA2CSoDZ^2` | Same horizontal point, 2m above street level |\n| `#7B6.63IH.XB8` | Albuquerque-area point with readability/checksum dots |\n| `#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2` | Multi-waypoint Hashpath-style arrival sequence |\n\n## Why not just use latitude/longitude or a map URL?\n\nLatitude/longitude is universal but awkward for humans.\n\nMap URLs work, but they are long, opaque, app-specific, and full of noise.\n\nHashsite gives the place itself a compact handle:\n\n```text\nreal place → short code\nshort code → real place\n```\n\n## Live app\n\n<https://hashsite.org>\n\n## Companion product\n\nHashpath is the live companion product for multi-step real-world instructions.\n\nHashsite gives places compact codes. Hashpath carries procedures around places: parking, gates, doors, codes, dropoff points, exits, and other arrival details.\n\n<https://hashpath.org>\n\n## Preserved original README material\n\nThe material below is the original README body, preserved rather than erased.\n\n<!-- HASHSITE_MENU_END -->\n'

if not readme.exists():
    print("ERROR: README.md not found. Run from the Hashsite repo root.", file=sys.stderr)
    sys.exit(1)

old = readme.read_text(encoding="utf-8")

if not backup.exists():
    backup.write_text(old, encoding="utf-8")
    print(f"Backed up existing README.md to {backup}")

pattern = re.compile(r"<!-- HASHSITE_MENU_BEGIN -->.*?<!-- HASHSITE_MENU_END -->\n?", re.S)
if pattern.search(old):
    new = pattern.sub(MENU.rstrip() + "\n\n", old)
    print("Replaced existing managed menu block.")
else:
    new = MENU.rstrip() + "\n\n" + old
    print("Prepended managed menu block and preserved existing README body.")

readme.write_text(new, encoding="utf-8")
