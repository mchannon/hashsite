![Hashsite banner](img/hashsitebanner.png)

# Hashsite

**Open geocoding. Works offline. No API key. No rent.**

Hashsite is a C library and coordinate format for encoding real-world locations as short, human-shareable alphadecimal strings. It is compact, hierarchical, 3D-native, and free to implement.

```
#7BA2CSoDZ          Amarillo, TX — 9-char, ~4m precision
#7B6.63IH.XB8       Albuquerque with Luhn dots
#7BA2CSoDZ^I1I      Same location, 1.5m above street level
#7BA2CKG^A#7BA2CSo#7BA2CSoDZ^J    Hashpath: gate → parking → door
```

**[Why Hashsite?](WHY.md)** — the case against proprietary geocoding and what Hashsite fixes.

**[Tech Specs](TECHSPECS.md)** — format reference, CLI, library API, import formats.

**[License](LICENSE.md)** — HPL-2.0: free for most uses, paid for government/enterprise.

---

## Quick start

```bash
gcc -O2 hashsite.c -lm -o hashsite

hashsite encode 35.222 -101.831 9     # -> #7BA2CSoDZ
hashsite decode 7BA2CSoDZ             # -> lat=35.222... lon=-101.831...
hashsite distance 7B663I 76B82D       # -> 2905.986 km
hashsite frommaidenhead FN31pr        # -> #7703K1QN  (ham radio grid)
hashsite fromnmea '$GPGGA,...'        # -> hashsite from GPS device output
```

Build and run `hashsite test` to verify your build against the full test suite.

---

## What is in this repository

| File | Purpose |
|---|---|
| `hashsite.c` | Complete C library + CLI (single file) |
| `hashsite.h` | Public API header |
| `hashsite.1` | Man page |
| `README.md` | This file |
| `WHY.md` | Why Hashsite exists and why the alternatives fall short |
| `TECHSPECS.md` | Format reference, CLI docs, library API |
| `LICENSE.md` | Hashsite Public License v2.0 |
| `licensing.md` | Licensing overview and Developer Welcome Kit |

---

## Companion: W3WNKER

**W3WNKER** (Worldwide 3D Wayfinding: iNteroperability Kernel for Emergency Response) is a separate companion project providing an offline, open codec for W3W-compatible addresses.

Free license: $0. Commercial license: $6,969.69. Retroactive scofflaw amnesty: $1.00. All licenses identical in all respects.

---

## Author

**Matt Channon** · licensing@hashsite.org · [hashsite.org](https://hashsite.org)
