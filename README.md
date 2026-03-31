![Hashsite banner](img/hashsitebanner.png)

# Hashsite

**License:** Hashsite Public License v2.0 (HPL-2.0) — see [LICENSE](LICENSE).
Not MIT. Not OSI open source. Free for personal and small-commercial use.
Commercial and government licensing: **$999 Developer Welcome Kit** — see [licensing.md](licensing.md).

**Author:** Matt Channon · **Contact:** licensing@hashsite.org

---

## What it is

Hashsite is a geocoding system and C library.

It encodes real-world locations as short alphadecimal strings that are compact enough to share in a text message, precise enough for doorstep-level navigation, hierarchical enough to shorten and compare by eye, and designed from the start to work offline.

Examples:

```
#7BA2CSoDZ
#7B663IHXB8
#F.6NZ^1
#WP1^A#WP2^3#WP3
```

Location is not solved by coordinates alone. It is solved by getting someone from where they are to where they need to be — past the gate, to the right entrance, on the right floor. Hashsite is built around that problem.

---

## The format

### Basic structure

Every Hashsite begins with `#`:

```
#7BA2CSoDZ
```

The `#` is required in canonical form. It is the visual marker that distinguishes a Hashsite from arbitrary alphanumeric noise.

The character set is `0–9` and `A–Z`. The letter `o` (lowercase) is always used in place of `O` (uppercase) to eliminate the most common visual ambiguity with the digit `0`. Input is case-insensitive. Canonical output is uppercase except for that one substitution.

### Precision

Each additional character subdivides the current cell by 6×6. Approximate precision at the equator:

| Characters | Cell size |
|---|---:|
| 1 | ~6679 km |
| 2 | ~1113 km |
| 3 | ~186 km |
| 4 | ~31 km |
| 5 | ~5 km |
| 6 | ~859 m |
| 7 | ~143 m |
| 8 | ~24 m |
| 9 | ~4 m |
| 10 | ~0.7 m |

Cells narrow toward the poles. Use `hashsite precision N lat` for latitude-aware dimensions.

In practice:

- 6 chars: neighborhood
- 7 chars: city block
- 8 chars: building entrance
- 9 chars: person-scale position
- 10 chars: sub-meter

### Hierarchy

Hashsite is prefix-hierarchical. The first character identifies a global zone. Each subsequent character subdivides that zone. This means:

- `#7B663I` is contained within `#7B663`
- `#7B663` is contained within `#7B6`
- Prefixes always contain their longer suffixes

You can shorten a Hashsite to get a coarser location, or extend it to get a finer one. Parent, child, and neighbor relationships are all computable without any external data.

### Readability dots

Hashsite supports optional Luhn-derived dots for human legibility:

```
#7B6.63IH.XB8
```

The dots are placed deterministically from the code content — they are not arbitrary. A dotted Hashsite describes the same location as the undotted one. The library can place and verify them.

Use dots when the code will be read aloud, transcribed by hand, or displayed in a context where visual grouping helps.

### Altitude

Append altitude after the `#CODE` using a `^` separator:

```
#7BA2CSoDZ^1       one meter above street level
#7BA2CSoDZ^S       ten meters below street level
#7BA2CSoDZ^I1I     1.5 meters above street level
#7BA2CSoDZ^255T    100001 meters above street level
```

The altitude encoding is base-36, big-endian. The first character after `^` is signed:

- `0` = 0 m
- `1`–`H` = +1 to +17 m
- `J`–`Z` = −1 to −17 m
- `I` = precision mode (sub-meter, see below)

Each additional character multiplies the range by 36. One character covers ±17 m; two covers ±647 m; three covers ±23 km; four covers ±838 km.

**Precision mode** begins with `^I` and adds sub-meter resolution. The character after `I` is the signed integer meter value; subsequent characters are fractional (each ÷36 of the previous):

```
#7BA2CSoDZ^I1I     1.5 m above street level
#7BA2CSoDZ^I00CYK5R  approximately 0.01 m above street level
#7BA2CSoDZ^IJI     −1.5 m (below street level)
```

Use `hashsite altencode` and `hashsite altdecode` to work with altitude strings directly.

### Hashpath

Multiple waypoints can be concatenated:

```
#7BA2CKG^A#7BA2CSo#7BA2CSoDZ^J
```

Each segment is `#CODE` with an optional `^ALT` suffix. The sequence describes an arrival path — not just a destination, but the sequence of points that gets someone there.

This is the right tool for:

- apartment complex navigation (gate → parking → staircase → door)
- hospital wayfinding (parking → entrance → elevator → clinic)
- airport pickup (curb → lane → standing point)
- delivery handoff (service gate → loading bay → final point)

---

## CLI

Build with `gcc -O2 hashsite.c -lm -o hashsite`.

### Encode and decode

```bash
hashsite encode 35.222 -101.831 9
# -> #7BA2CSoDZ

hashsite decode 7BA2CSoDZ
# -> lat=35.222... lon=-101.831...

hashsite decode 7BA2CSoDZ^A
# -> lat=35.222... lon=-101.831...
# -> alt=10.0000 m above street level

hashsite bbox 7B663I
# -> full bounding box and cell dimensions
```

### Inspection

```bash
hashsite valid 7B663IHXB8        # exits 0 if valid
hashsite precision 9              # cell size at 9 chars
hashsite precision 9 35.0         # latitude-aware dimensions
hashsite parent 7B663IHXB8        # -> #7B663IHX (one char shorter)
hashsite contains 7B663 7B663IHXB8  # exits 0 if first contains second
```

### Altitude

```bash
hashsite altencode 10             # -> ^A
hashsite altencode 1.5            # -> ^I1I  (auto-selects precision mode)
hashsite altencode 100001         # -> ^255T
hashsite altencode -10            # -> ^S
hashsite altdecode "^I1I"         # -> 1.5000000 m
hashsite altdecode "^255T"        # -> 100001.0000000 m
```

### Geometry

```bash
hashsite distance 7B663I 76B82D
# -> 2905.986 km

hashsite distance3d 7B663I 0 76B82D 1000
# -> 2905.986 km  (altitude difference negligible at this range)

hashsite bearing 7B663I 76B82D
# -> 67.86 degrees (ENE)

hashsite midpoint 7B663I 76B82D
# -> #74EVoC

hashsite midpoint3d 7B663I 0 76B82D 200
# -> #74EVoC^2S  (midpoint at 100m altitude)

hashsite offset 7B663IHXB8 100 50
# -> translate 100m north, 50m east

hashsite offset3d 7B663IHXB8 10 0 50 5
# -> translate 50m east, 5m up from 10m altitude

hashsite neighbors 7B663I
# -> up to 8 adjacent cells

hashsite children 7B663I
# -> all 36 sub-cells
```

### Dots

```bash
hashsite luhn 7B663IHXB8
# -> #7B6.63IH.XB8

hashsite luhncheck 7B6.63IH.XB8
# -> exits 0 if dots are correctly placed
```

### Closest: suffix pattern matching

`closest` finds the geographically nearest Hashsite matching a suffix pattern.

**Pattern operators:**

| Pattern | Meaning |
|---|---|
| `$SUFFIX` | Keep same total length as your current position, fill the end with SUFFIX |
| `$$SUFFIX` | Explicit 2-char prefix + SUFFIX |
| `$$$SUFFIX` | Explicit 3-char prefix + SUFFIX |
| `%SUFFIX` | Drop 5 chars from your position length, then fill with SUFFIX |
| `%%SUFFIX` | Drop 10 chars, then fill with SUFFIX |
| `SUFFIX` | Fixed location — no prefix computation |

The `$` operator matches your current position's total length, filling the suffix from the end. Think of it as "find the nearest code with this ending at my current precision."

The `%` operator produces a shorter, coarser result — useful when you want to find the nearest region (not just cell) ending in a particular suffix.

```bash
hashsite closest 7B663IHXB8 '$XB8'
# -> nearest code ending in XB8 at 10-char precision near Albuquerque

hashsite closest 7B663IHXB8 '$$$XB8'
# -> nearest 3-char-prefix + XB8 = 9-char code near Albuquerque

hashsite closest 7B663IHXB8 '%XB8'
# -> nearest code at (10−5)=5-char prefix + XB8 = 8-char total

hashsite closest 62AZZ492 '$00009'
# -> #62H00009  (nearest 8-char code ending in 00009)
```

---

## Coordinate format import

Hashsite can convert from many coordinate formats directly. All `from*` commands accept an optional final `nchars` argument for output precision (default varies by source format).

### Geocode systems

```bash
hashsite fromgeohash 9q8yy 9
# -> San Francisco as 9-char hashsite

hashsite frompluscode 9C3X+GV5C 9
# -> London as hashsite

hashsite frommaidenhead FN31pr
# -> #7703K1QN  (W1AW, Newington CT — auto-precision from 6-char grid)

hashsite fromgars 147LL
# -> #7AB59  (Albuquerque area, 30-minute GARS cell)

hashsite fromgeoref MK1406
# -> London area at 1-degree precision
```

### Surveyor and GPS formats

```bash
hashsite fromdms "40d42m51sN" "-74.0060"
# -> New York (DMS accepts many formats: 40°42'51"N, 40:42:51N, etc.)

hashsite fromnmea '$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18'
# -> #68SPK09K3^9  (San Francisco with altitude from GGA sentence)
# Also accepts $GPRMC sentences. Validates NMEA checksum.

hashsite fromutm "18T 583960 4507523"
# -> #76B82D7  (New York — spherical approximation, ~50m accuracy)
```

Supported input formats: Geohash, Plus Code (OLC), Maidenhead (ham radio grid squares), GARS (DoD/Civil Air Patrol), GEOREF (aviation/NATO), DMS (degrees/minutes/seconds), DDM (degrees/decimal minutes), NMEA GGA, NMEA RMC, UTM (spherical approximation).

---

## Library API

Include `hashsite.h` and link with `hashsite.c -lm`.

### Core

```c
void ll2hsps(double lat, double lon, int nchars, char *buf);
int  hsps2ll(const char *hs, double *lat_out, double *lon_out);
int  hsps2bbox(const char *hs, hs_bbox *bbox);
```

### Inspection

```c
int    hs_clean(const char *in, char *buf);
int    hs_valid(const char *in);
double hs_precision_m(int nchars);
void   hs_precision_at(double lat_deg, int nchars, double *hgt_m, double *wid_m);
int    hs_parent(const char *in, char *out);
int    hs_contains(const char *a, const char *b);
```

### Altitude

```c
int    hs_alt_encode(double meters, int precision, char *out);
double hs_alt_decode(const char *s);
int    hs_alt_encode_auto(double meters, char *out);

#define HS_ALT_NONE  (1e308)   /* sentinel: no altitude present */
#define HS_ALT_MAXLEN 16       /* max chars in a vertical string */
```

### Geometry (2D)

```c
double hs_distance_m(const char *a, const char *b);
double hs_bearing(const char *a, const char *b);
int    hs_midpoint(const char *a, const char *b, char *out);
int    hs_offset(const char *in, double north_m, double east_m, char *out);
int    hs_neighbors(const char *in, char neighbors[][HS_MAXLEN + 1]);
int    hs_children(const char *in, char children[][HS_MAXLEN + 1]);
int    hs_guess_closest(const char *user_hs, const char *pattern, char *result);
```

### Geometry (3D)

```c
double hs_distance3d_m(const char *a, double a_alt,
                       const char *b, double b_alt);
int    hs_offset3d(const char *in, double in_alt,
                   double north_m, double east_m, double up_m,
                   char *out, double *out_alt);
int    hs_midpoint3d(const char *a, double a_alt,
                     const char *b, double b_alt,
                     char *out, double *out_alt);
```

### Paths

```c
typedef struct {
    double lat;
    double lon;
    double alt_m;           /* HS_ALT_NONE if absent */
    char   code[HS_MAXLEN + 1];
    int    nchars;
} hs_waypoint;

void hs_encode_path(hs_waypoint *wps, int nwps, int nchars_each, char *buf);
int  hs_decode_path(const char *in, hs_waypoint *wps, int max_wps);
```

### Dots

```c
int hs_luhn_place(const char *in, char *out);
int hs_luhn_check(const char *in);
```

### Import from other formats

```c
/* Geocode systems */
int hs_from_geohash   (const char *geohash,  int nchars, char *out);
int hs_from_pluscode  (const char *pluscode, int nchars, char *out);
int hs_from_maidenhead(const char *loc,      int nchars, char *out);
int hs_from_gars      (const char *gars,     int nchars, char *out);
int hs_from_georef    (const char *gr,       int nchars, char *out);

/* Surveyor / GPS formats */
int hs_from_dms      (const char *lat_s, const char *lon_s, int nchars, char *out);
int hs_from_nmea_gga (const char *sentence, int nchars, char *out, double *alt_out);
int hs_from_nmea_rmc (const char *sentence, int nchars, char *out);
int hs_from_utm      (const char *s,         int nchars, char *out);

/* Raw parsers (return lat/lon) */
int    hs_parse_maidenhead(const char *loc, double *lat_out, double *lon_out);
int    hs_parse_gars      (const char *gars, double *lat_out, double *lon_out);
int    hs_parse_georef    (const char *gr,   double *lat_out, double *lon_out);
int    hs_parse_dms       (const char *s,    double *deg_out);
int    hs_parse_ddm       (const char *s,    double *deg_out);
int    hs_parse_nmea_gga  (const char *sentence,
                           double *lat_out, double *lon_out, double *alt_out);
int    hs_parse_nmea_rmc  (const char *sentence,
                           double *lat_out, double *lon_out);
int    hs_parse_utm       (const char *s,    double *lat_out, double *lon_out);
```

All `nchars <= 0` → auto-select precision based on source format.

---

## Design notes

**Offline-first.** Encode and decode require no network access, no API key, no server. The full codec runs on any device that can compile C.

**Hierarchical.** Prefixes contain their extensions. A 4-char Hashsite is the parent of all 5-char Hashsites that begin with it.

**Equal-area latitude bands.** The first two characters use latitude-aware subdivisions at 0°, 19.47°, and 41.81°, keeping cells more equal in area than a naive rectangular grid. Polar zones use a column-count scheme that prevents the extreme longitude crowding that plagues other systems at high latitudes.

**No O/0 ambiguity.** The letter O is always output as lowercase `o`. This is the only case where lowercase appears in canonical output. Input is case-insensitive throughout.

**3D is native, not bolted on.** Altitude encoding is part of the format specification, not an afterthought. Precision mode supports sub-millimeter vertical resolution when needed.

**Path-first thinking.** A real arrival problem is rarely a single point. Hashpath is a first-class construct, not an API convenience.

---

## Companion: W3WNKER

**W3WNKER** (Worldwide 3D Wayfinding: iNteroperability Kernel for Emergency Response) is a separate companion project that provides offline, open decoding of W3W-compatible addresses.

Hashsite is the destination. W3WNKER is the escape hatch for users currently locked into a proprietary word-based location system.

Licenses: Free (HPL). Commercial: $6,969.69. Retroactive (scofflaw amnesty): $1.00. All licenses identical.

---

## Roadmap

- [x] C library and CLI
- [x] 2D and 3D geometry
- [x] Altitude encoding (coarse and precision modes)
- [x] Luhn dot placement and verification
- [x] Hashpath encode/decode
- [x] Geohash, Plus Code, Maidenhead, GARS, GEOREF, DMS, NMEA, UTM import
- [ ] WebAssembly / npm package
- [ ] Python package (PyPI)
- [ ] Swift package (iOS/macOS)
- [ ] Android library (JNI/NDK)
- [ ] QGIS plugin
- [ ] Web demo (hashsite.org)
- [ ] Test vector file (language-agnostic reference)
- [ ] MGRS/USNG import (requires ellipsoidal TM math)
- [ ] OS National Grid import (UK)
- [ ] Rumbleramble haptic navigation mode (iOS)

---

## License

**Hashsite Public License v2.0 (HPL-2.0)**

Free for personal use and small commercial use. A paid license is required for governments, militaries, intelligence agencies, law enforcement, large enterprises, and contractors acting on their behalf.

**Developer Welcome Kit: $999** — 3-year term, up to 5 developers, one legal entity, one product.

See [LICENSE](LICENSE), [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md), [licensing.md](licensing.md).

Licensing contact: **licensing@hashsite.org**
