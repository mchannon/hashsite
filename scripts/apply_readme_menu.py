#!/usr/bin/env python3
from pathlib import Path
import re
import sys

readme = Path("README.md")
backup = Path("README.before-hashsite-menu.bak.md")
MENU = "<!-- HASHSITE_MENU_BEGIN -->\n\n# Hashsite\n\n![Hashsite banner](img/hashsitebanner.png)\n\n**Open geocoding. Can be done with pencil and paper. Works offline. No API key. No rent. Locations that work for humans.**\n\nHashsite is a C library, CLI, web app, and coordinate format for encoding real-world locations as short, human-shareable alphadecimal strings.\n\n| Code | Lat, Lon | Notes |\n|---|---|---|\n| `#7BA2` | 35.22°N, 101.76°W | Potter County, TX — 4-char, ~40km precision |\n| `#7BA2CSoDZ` | 35.2220°N, 101.8310°W | Cadillac Ranch, Amarillo TX — 9-char, ~5m precision |\n| `#7BA2CSoDZ^2` | 35.2220°N, 101.8310°W | Same horizontal point, 2m above street level |\n| `$FC64W` | 34.927°N, 101.663°W | From `#7BA2CSoDZ`: nearest 8-char code ending `FC64W` → `#7BAFC64W` |\n| `#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2` | 33.628°N, 101.905°W | Hashpath: gate → code → parking → stairs → door +2m |\n| `#7B6.63IH.XB8` | 35.1240°N, 106.5692°W | Albuquerque — 10-char, ~1m precision, with checksum dots |\n\n## Start here\n\n| Topic | Page |\n|---|---|\n| 1. Why Hashsite? | [`docs/01-WHY-HASHSITE.md`](docs/01-WHY-HASHSITE.md) |\n| 2. Format, codes, and precision | [`docs/02-FORMAT-CODES-PRECISION.md`](docs/02-FORMAT-CODES-PRECISION.md) |\n| 3. Grid structure and hierarchy | [`docs/03-GRID-STRUCTURE.md`](docs/03-GRID-STRUCTURE.md) |\n| 4. Altitude and 3D | [`docs/04-ALTITUDE-AND-3D.md`](docs/04-ALTITUDE-AND-3D.md) |\n| 5. Readability, checksums, and dots | [`docs/05-READABILITY-CHECKSUMS-DOTS.md`](docs/05-READABILITY-CHECKSUMS-DOTS.md) |\n| 6. Hashpaths | [`docs/06-HASHPATHS.md`](docs/06-HASHPATHS.md) |\n| 7. CLI reference with outputs | [`docs/07-CLI-REFERENCE.md`](docs/07-CLI-REFERENCE.md) |\n| 8. Library API | [`docs/08-LIBRARY-API.md`](docs/08-LIBRARY-API.md) |\n| 9. Coordinate import with outputs | [`docs/09-COORDINATE-IMPORT.md`](docs/09-COORDINATE-IMPORT.md) |\n| 10. Pattern matching and suffixes | [`docs/10-PATTERN-MATCHING.md`](docs/10-PATTERN-MATCHING.md) |\n| 11. Web app behavior | [`docs/11-WEB-APP.md`](docs/11-WEB-APP.md) |\n| 12. Design and build philosophy | [`docs/12-DESIGN-BUILD-PHILOSOPHY.md`](docs/12-DESIGN-BUILD-PHILOSOPHY.md) |\n| 13. Word mode and legacy ideas | [`docs/13-WORD-MODE-AND-LEGACY-IDEAS.md`](docs/13-WORD-MODE-AND-LEGACY-IDEAS.md) |\n| 14. Roadmap, W3WNKER, license, and companions | [`docs/14-ROADMAP-W3WNKER-LICENSE-COMPANIONS.md`](docs/14-ROADMAP-W3WNKER-LICENSE-COMPANIONS.md) |\n\n## Quick start\n\n```bash\ngcc -O2 hashsite.c -lm -o hashsite\n./hashsite test\n```\n\n```bash\nhashsite encode 35.222 -101.831 9     # -> #7BA2CSoDZ\nhashsite decode 7BA2CSoDZ             # -> lat=35.222... lon=-101.831...\nhashsite distance 7B663I 76B82D       # -> 2905.986 km\nhashsite frommaidenhead FN31pr        # -> #7703K1QN\nhashsite fromnmea '$GPGGA,...'        # -> hashsite + altitude from GPS device\n```\n\n## Live app\n\n<https://hashsite.org>\n\n## Companion product\n\nHashpath is the live companion product for multi-step real-world instructions: parking, gates, doors, codes, dropoff points, exits, and other arrival details.\n\n<https://hashpath.org>\n\n<!-- HASHSITE_MENU_END -->\n"

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
