#!/usr/bin/env python3
from pathlib import Path
import re
import sys

readme = Path("README.md")
backup = Path("README.before-hashsite-menu.bak.md")

MENU = """<!-- HASHSITE_MENU_BEGIN -->

# Hashsite

![Hashsite banner](img/hashsitebanner.png)

**Open geocoding. Short letters and numbers for real-world places. Offline-capable. No API key. No rent.**

Hashsite encodes real-world locations as compact, human-shareable alphadecimal strings.

A Hashsite can be short enough to text, print, speak, write on a sticky note, put in a QR code, or paste into another system:

```text
#7BA2CSoDZ
#7B6.63IH.XB8
#7BA2CSoDZ^2
```

The map app is the interface.  
The code is the durable object.

## Start here

Hashsite has outgrown a single infinite-scroll README. This README is the front door; the deeper material is split into topic pages.

| Topic | Page |
|---|---|
| What Hashsite is | [`docs/01-WHAT-IS-A-HASHSITE.md`](docs/01-WHAT-IS-A-HASHSITE.md) |
| Code format, alphabet, precision, and rubric | [`docs/02-CODES-AND-RUBRIC.md`](docs/02-CODES-AND-RUBRIC.md) |
| Grid and encoding model | [`docs/03-GRID-AND-ENCODING.md`](docs/03-GRID-AND-ENCODING.md) |
| Altitude / 3D locations | [`docs/04-ALTITUDE.md`](docs/04-ALTITUDE.md) |
| Dots and readability checks | [`docs/05-DOTS-AND-READABILITY.md`](docs/05-DOTS-AND-READABILITY.md) |
| Hashpaths in the Hashsite library | [`docs/06-HASHPATHS-IN-HASHSITE.md`](docs/06-HASHPATHS-IN-HASHSITE.md) |
| CLI reference | [`docs/07-CLI-REFERENCE.md`](docs/07-CLI-REFERENCE.md) |
| Library API | [`docs/08-LIBRARY-API.md`](docs/08-LIBRARY-API.md) |
| Coordinate import and interoperability | [`docs/09-COORDINATE-IMPORT.md`](docs/09-COORDINATE-IMPORT.md) |
| Web app behavior | [`docs/10-WEB-APP.md`](docs/10-WEB-APP.md) |
| Design principles | [`docs/11-DESIGN-PRINCIPLES.md`](docs/11-DESIGN-PRINCIPLES.md) |
| Roadmap | [`docs/12-ROADMAP.md`](docs/12-ROADMAP.md) |
| Companion product: Hashpath | [`docs/13-COMPANION-HASHPATH.md`](docs/13-COMPANION-HASHPATH.md) |
| Preserved original README material | [below](#preserved-original-readme-material) |

## One-minute version

Hashsite is a coordinate format, library, CLI, and web app for turning real-world locations into short alphadecimal codes.

It is meant to be:

- compact
- offline-capable
- hierarchical
- human-handleable
- machine-decodable
- 2D and 3D aware
- open to implement
- useful without renting an API

## Examples

| Code | Meaning |
|---|---|
| `#7BA2` | Potter County, TX area — coarse, 4-character Hashsite |
| `#7BA2CSoDZ` | Cadillac Ranch / Amarillo-area point — person-scale precision |
| `#7BA2CSoDZ^2` | Same horizontal point, 2m above street level |
| `#7B6.63IH.XB8` | Albuquerque-area point with readability/checksum dots |
| `#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2` | Multi-waypoint Hashpath-style arrival sequence |

## Why not just use latitude/longitude or a map URL?

Latitude/longitude is universal but awkward for humans.

Map URLs work, but they are long, opaque, app-specific, and full of noise.

Hashsite gives the place itself a compact handle:

```text
real place → short code
short code → real place
```

## Live app

<https://hashsite.org>

## Companion product

Hashpath is the live companion product for multi-step real-world instructions.

Hashsite gives places compact codes. Hashpath carries procedures around places: parking, gates, doors, codes, dropoff points, exits, and other arrival details.

<https://hashpath.org>

## Preserved original README material

The material below is the original README body, preserved rather than erased. The topic pages above make that material easier to navigate, but the older explanation remains part of the project record.

<!-- HASHSITE_MENU_END -->
"""

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
