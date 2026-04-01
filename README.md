![Hashsite banner](img/hashsitebanner.png)

# Hashsite

**Open geocoding. Works offline. No API key. No rent.**

Hashsite is a C library and coordinate format for encoding real-world locations as short, human-shareable alphadecimal strings. Compact, hierarchical, 3D-native, and free to implement.

```
#7BA2CSoDZ          Amarillo, TX — 9-char, ~4m precision
#7B6.63IH.XB8       Albuquerque with Luhn readability dots
#7BA2CSoDZ^I1I      Same location, 1.5m above street level
#7BA2CKG^A#7BA2CSo#7BA2CSoDZ^J    Hashpath: gate → parking → door
```

---

## Documents

**[WHY.md](WHY.md)** — The case against proprietary geocoding and what Hashsite fixes.

**[TECHSPECS.md](TECHSPECS.md)** — Format reference, CLI, library API, coordinate import formats.

**[LICENSE.md](LICENSE.md)** — Hashsite Public License v2.0. Free for most uses; $999 Developer Welcome Kit for commercial and government use.

---

## Quick start

```bash
gcc -O2 hashsite.c -lm -o hashsite

hashsite encode 35.222 -101.831 9     # -> #7BA2CSoDZ
hashsite decode 7BA2CSoDZ             # -> lat=35.222... lon=-101.831...
hashsite distance 7B663I 76B82D       # -> 2905.986 km
hashsite frommaidenhead FN31pr        # -> #7703K1QN  (ham radio grid square)
hashsite fromnmea '$GPGGA,...'        # -> hashsite + altitude from GPS device
hashsite test                         # -> run full test suite
```

---

## Files

| File | Purpose |
|---|---|
| `hashsite.c` | Complete C library + CLI (single file, no dependencies beyond libm) |
| `hashsite.h` | Public API header |
| `hashsite.1` | Man page |
| `vectors.json` | Test vectors for port verification and patent exhibit |
| `WHY.md` | Advocacy and competitive analysis |
| `TECHSPECS.md` | Technical reference |
| `LICENSE.md` | HPL-2.0 license terms |

---

## W3WNKER

**W3WNKER** (Worldwide 3D Wayfinding: iNteroperability Kernel for Emergency Response) is a companion project providing an offline, open codec for W3W-compatible addresses.

Free: $0. Commercial: $6,969.69. Retroactive amnesty: $1.00. All licenses identical.

---

**Matt Channon** · licensing@hashsite.org · [hashsite.org](https://hashsite.org)
