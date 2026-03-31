![Hashsite banner](img/hashsitebanner.png)

# Hashsite Technical Specifications

This document covers the Hashsite format, CLI, and C library API.

**[Why Hashsite?](WHY.md)** — start here if you want the motivation before the mechanics.

---

## The format

### Basic structure

Every Hashsite begins with `#`:

```
#7BA2CSoDZ
```

The `#` is required in canonical form. It is the visual marker that distinguishes a Hashsite from arbitrary alphanumeric text.

The character set is `0–9` and `A–Z`. The letter `o` (lowercase) is always used in place of `O` (uppercase) to eliminate the most common visual ambiguity with the digit `0`. Input is case-insensitive. Canonical output is uppercase except for that one substitution.

### Precision

Each additional character subdivides the current cell by 6×6. Approximate precision at the equator:

| Characters | Cell size | Practical use |
|---|---:|---|
| 1 | ~6679 km | Continental |
| 2 | ~1113 km | Country scale |
| 3 | ~186 km | Metro area |
| 4 | ~31 km | City |
| 5 | ~5 km | District |
| 6 | ~859 m | Neighborhood |
| 7 | ~143 m | City block |
| 8 | ~24 m | Building entrance |
| 9 | ~4 m | Person-scale position |
| 10 | ~0.7 m | Sub-meter |

Cells narrow toward the poles. Use `hashsite precision N lat` for latitude-aware dimensions at a specific latitude.

### Hierarchy

Hashsite is prefix-hierarchical:

- `#7B663I` is contained within `#7B663`
- `#7B663` is contained within `#7B6`
- Prefixes always contain their longer suffixes

You can shorten a Hashsite to get a coarser location, or extend it to get a finer one. Parent, child, and neighbor relationships are all computable without any external data.

### Grid structure

The first two characters use latitude-aware subdivisions at 0°, 19.47°, and 41.81°, keeping cells more equal in area than a naive rectangular grid. Polar zones use a variable-width column scheme (`1/1/2/3/3/4/5/5/6/6`) that prevents extreme longitude crowding at high latitudes. All subsequent characters use regular 6×6 subdivision.

### Readability dots

Hashsite supports optional Luhn-derived dots for human legibility:

```
#7B6.63IH.XB8
```

The dots are placed deterministically from the code content — not arbitrarily. A dotted Hashsite describes the same location as the undotted one. The library can place and verify them. Use dots when the code will be read aloud, transcribed by hand, or displayed in a context where visual grouping reduces transcription errors.

### Altitude

Append altitude after `#CODE` using `^`:

```
#7BA2CSoDZ^1       +1 m above street level
#7BA2CSoDZ^S       −10 m below street level
#7BA2CSoDZ^I1I     +1.5 m above street level
#7BA2CSoDZ^255T    +100001 m above street level
```

**Coarse mode** — the first character after `^` is signed base-36:

| Character | Value |
|---|---|
| `0` | 0 m |
| `1`–`H` | +1 to +17 m |
| `J`–`Z` | −1 to −17 m |
| `I` | switch to precision mode |

Each additional character extends the range by ×36: one char = ±17 m, two = ±647 m, three = ±23 km, four = ±838 km. Always big-endian — most significant digit first.

**Precision mode** — begins with `^I`. The character after `I` is the signed integer meter value; subsequent characters are fractional (each ÷36 of the previous). `I` as first-after-`I` encodes a negative sub-meter zero.

```
#7BA2CSoDZ^I1I       +1.5 m
#7BA2CSoDZ^I00CYK5R  +0.01 m (approximately)
#7BA2CSoDZ^IJI       −1.5 m
```

`HS_ALT_NONE` (value `1e308`) is the sentinel for "no altitude present" in waypoint structures.

### Hashpath

Multiple waypoints concatenated with `#` separators:

```
#7BA2CKG^A#7BA2CSo#7BA2CSoDZ^J
```

Each segment is `#CODE` with an optional `^ALT` suffix. Represents an ordered arrival sequence. The library encodes and decodes hashpaths through `hs_encode_path()` and `hs_decode_path()`.

---

## Build

```bash
gcc -O2 hashsite.c -lm -o hashsite
```

Single file. No dependencies beyond `libm`. C99 or later. Runs on Linux, macOS, Windows (MinGW), embedded targets.

---

## CLI reference

### Encode and decode

```bash
hashsite encode 35.222 -101.831 9
# -> #7BA2CSoDZ

hashsite encode 35.222 -101.831       # default 10 chars
# -> #7BA2CSoDZ5S

hashsite decode 7BA2CSoDZ
# -> lat=35.22195... lon=-101.83116...

hashsite decode 7BA2CSoDZ^A
# -> lat=35.22195... lon=-101.83116...
# -> alt=10.0000 m above street level

hashsite bbox 7B663I
# -> lat_s=35.075... lat_n=35.216... lon_w=-106.650... lon_e=-106.390...
# -> height=15.77 km  width=22.73 km
```

### Inspection

```bash
hashsite valid 7B663IHXB8          # exits 0 if valid
hashsite valid 7B663IHXB8ZZZ       # exits 1 if invalid

hashsite precision 9               # ~4.0 m (equatorial)
hashsite precision 9 35.0          # latitude-aware: height × width in meters

hashsite parent 7B663IHXB8         # -> #7B663IHX
hashsite contains 7B663 7B663IHXB8 # exits 0 (yes, 7B663 contains the longer code)
```

### Altitude

```bash
hashsite altencode 10              # -> ^A
hashsite altencode -10             # -> ^S
hashsite altencode 1.5             # -> ^I1I  (auto precision mode)
hashsite altencode 100001          # -> ^255T
hashsite altencode 0.01            # -> ^I00CYK5R
hashsite altencode 0.01 p          # -> force precision mode

hashsite altdecode "^A"            # -> 10.0000000 m
hashsite altdecode "^I1I"          # -> 1.5000000 m
hashsite altdecode "^255T"         # -> 100001.0000000 m
```

### Geometry — 2D

```bash
hashsite distance 7B663I 76B82D
# -> 2905.986 km

hashsite bearing 7B663I 76B82D
# -> 67.86 degrees (ENE)

hashsite midpoint 7B663I 76B82D
# -> #74EVoC

hashsite offset 7B663IHXB8 100 50
# -> translate 100 m north, 50 m east, same precision

hashsite neighbors 7B663I
# -> up to 8 adjacent cells at same precision

hashsite children 7B663I
# -> all 36 sub-cells (one character longer)
```

### Geometry — 3D

```bash
hashsite distance3d 7B663I 0 76B82D 1000
# -> 2905.986 km  (1 km altitude difference negligible at this range)

hashsite midpoint3d 7B663I 0 76B82D 200
# -> #74EVoC^2S  (midpoint at 100 m altitude)

hashsite offset3d 7B663IHXB8 10 0 50 5
# -> CODE^ALT  (50 m east, 5 m up from altitude 10 m)
```

### Dots

```bash
hashsite luhn 7B663IHXB8
# -> #7B6.63IH.XB8

hashsite luhncheck 7B6.63IH.XB8
# -> exits 0 if dots are correctly placed, 1 if not
```

### Pattern matching

`closest` finds the geographically nearest Hashsite matching a suffix pattern near your current position.

```bash
hashsite closest 7B663IHXB8 '$XB8'
# -> nearest code ending in XB8 at full 10-char precision

hashsite closest 7B663IHXB8 '$$$XB8'
# -> nearest 3-char-prefix + XB8 = 9-char code

hashsite closest 7B663IHXB8 '%XB8'
# -> nearest code: (10−5)=5-char prefix + XB8 = 8-char total

hashsite closest 62AZZ492 '$00009'
# -> #62H00009
```

**Pattern syntax:**

| Pattern | Prefix length | Result length |
|---|---|---|
| `$SUFFIX` | user_len − suf_len | user_len |
| `$$SUFFIX` | 2 | 2 + suf_len |
| `$$$SUFFIX` | 3 | 3 + suf_len |
| `%SUFFIX` | user_len − 5 − suf_len | user_len − 5 |
| `%%SUFFIX` | user_len − 10 − suf_len | user_len − 10 |
| `SUFFIX` | 0 (fixed) | suf_len |

`$` — match your current total position length; the suffix fills from the end. One dollar sign means "find me the nearest code that ends in this suffix and is the same length as my position."

`%` — each percent sign drops 5 characters from your position length. Useful when you want a coarser result that still ends in a memorable suffix.

### Coordinate format import

All `from*` commands accept an optional `nchars` argument (default: auto from source precision).

```bash
# Geocode systems
hashsite fromgeohash 9q8yy 9
hashsite frompluscode 9C3X+GV5C 9
hashsite frommaidenhead FN31pr          # ham radio grid square
hashsite fromgars 147LL                 # DoD/Civil Air Patrol
hashsite fromgeoref MK1406              # aviation / NATO

# Surveyor and GPS formats
hashsite fromdms "40d42m51sN" "-74.0060"
hashsite fromdms "40°42'51\"N" "74°0'21\"W"
hashsite fromdms "40:42:51N" "74:0:21W"

hashsite fromnmea '$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18'
# -> #68SPK09K3^9  (includes altitude from GGA sentence)
# Also accepts $GPRMC. Validates NMEA checksum.

hashsite fromutm "18T 583960 4507523"   # spherical approximation, ~50 m accuracy
```

Supported input formats: Geohash, Plus Code (OLC), Maidenhead (ham radio), GARS (DoD/CAP), GEOREF (aviation/NATO), DMS (degrees/minutes/seconds), DDM (degrees/decimal minutes), NMEA GGA, NMEA RMC, UTM.

---

## Library API

Include `hashsite.h`, link with `hashsite.c -lm`.

### Core encode/decode

```c
void ll2hsps(double lat, double lon, int nchars, char *buf);
int  hsps2ll  (const char *hs, double *lat_out, double *lon_out);
int  hsps2bbox(const char *hs, hs_bbox *bbox);
```

`hs_bbox` contains `lat_s`, `lat_n`, `lon_w`, `lon_e`, `lat_c`, `lon_c`.

### Inspection

```c
int    hs_clean(const char *in, char *buf);         /* strip #, dots, ^ */
int    hs_valid(const char *in);
double hs_precision_m(int nchars);
void   hs_precision_at(double lat_deg, int nchars,
                       double *hgt_m, double *wid_m);
int    hs_parent(const char *in, char *out);
int    hs_contains(const char *a, const char *b);
```

### Altitude

```c
#define HS_ALT_NONE   (1e308)  /* sentinel: no altitude */
#define HS_ALT_MAXLEN 16       /* max vertical string length */

int    hs_alt_encode     (double meters, int precision, char *out);
double hs_alt_decode     (const char *s);
int    hs_alt_encode_auto(double meters, char *out);
```

`precision` = 0 for coarse mode (integer meters), 1 for precision mode (sub-meter). `hs_alt_encode_auto` selects automatically.

### Geometry — 2D

```c
double hs_distance_m (const char *a, const char *b);
double hs_bearing    (const char *a, const char *b);
int    hs_midpoint   (const char *a, const char *b, char *out);
int    hs_offset     (const char *in,
                      double north_m, double east_m, char *out);
int    hs_neighbors  (const char *in,
                      char neighbors[][HS_MAXLEN + 1]);
int    hs_children   (const char *in,
                      char children[][HS_MAXLEN + 1]);
int    hs_guess_closest(const char *user_hs,
                        const char *pattern, char *result);
```

### Geometry — 3D

```c
double hs_distance3d_m(const char *a, double a_alt,
                       const char *b, double b_alt);
int    hs_offset3d    (const char *in, double in_alt,
                       double north_m, double east_m, double up_m,
                       char *out, double *out_alt);
int    hs_midpoint3d  (const char *a, double a_alt,
                       const char *b, double b_alt,
                       char *out, double *out_alt);
```

### Paths

```c
typedef struct {
    double lat;
    double lon;
    double alt_m;              /* HS_ALT_NONE if absent */
    char   code[HS_MAXLEN + 1];
    int    nchars;
} hs_waypoint;

void hs_encode_path(hs_waypoint *wps, int nwps,
                    int nchars_each, char *buf);
int  hs_decode_path(const char *in,
                    hs_waypoint *wps, int max_wps);
```

`buf` for `hs_encode_path` must be at least `(1 + HS_MAXLEN + HS_ALT_MAXLEN + 2) * nwps` bytes.

### Dots

```c
int hs_luhn_place(const char *in, char *out);  /* out: HS_MAXLEN+3 */
int hs_luhn_check(const char *in);
```

### Coordinate format parsers

All `hs_from_*` wrappers return `nchars` on success, `0` on error. `nchars <= 0` selects precision automatically from the source format.

```c
/* Geocode systems */
int hs_from_geohash   (const char *geohash,  int nchars, char *out);
int hs_from_pluscode  (const char *pluscode, int nchars, char *out);
int hs_from_maidenhead(const char *loc,      int nchars, char *out);
int hs_from_gars      (const char *gars,     int nchars, char *out);
int hs_from_georef    (const char *gr,       int nchars, char *out);

/* Surveyor / GPS formats */
int hs_from_dms      (const char *lat_s, const char *lon_s,
                      int nchars, char *out);
int hs_from_nmea_gga (const char *sentence, int nchars,
                      char *out, double *alt_out);
int hs_from_nmea_rmc (const char *sentence, int nchars, char *out);
int hs_from_utm      (const char *s,        int nchars, char *out);

/* Raw parsers — return lat/lon in decimal degrees */
int    hs_parse_maidenhead(const char *loc,
                           double *lat_out, double *lon_out);
int    hs_parse_gars      (const char *gars,
                           double *lat_out, double *lon_out);
int    hs_parse_georef    (const char *gr,
                           double *lat_out, double *lon_out);
int    hs_parse_dms       (const char *s,   double *deg_out);
int    hs_parse_ddm       (const char *s,   double *deg_out);
int    hs_parse_nmea_gga  (const char *sentence,
                           double *lat_out, double *lon_out,
                           double *alt_out);
int    hs_parse_nmea_rmc  (const char *sentence,
                           double *lat_out, double *lon_out);
int    hs_parse_utm       (const char *s,
                           double *lat_out, double *lon_out);
```

---

## Constants

```c
#define HS_MAXLEN     18   /* max alphadecimal chars in a hashsite */
#define HS_ALT_MAXLEN 16   /* max chars in a vertical string */
#define HS_ALT_NONE   (1e308)  /* sentinel: no altitude */
```

---

## Coordinate system coverage

| System | Status |
|---|---|
| Geohash | ✅ Import |
| Plus Code (OLC) | ✅ Import |
| Maidenhead | ✅ Import |
| GARS | ✅ Import |
| GEOREF | ✅ Import |
| DMS / DDM | ✅ Import |
| NMEA GGA / RMC | ✅ Import |
| UTM | ✅ Import (spherical approx., ~50 m) |
| MGRS / USNG | Planned (requires ellipsoidal TM) |
| OS National Grid | Planned |
| State Plane | Planned |

---

## Roadmap

- [x] C library and CLI — complete
- [x] 2D and 3D geometry — complete
- [x] Altitude encoding (coarse and precision) — complete
- [x] Luhn dot placement and verification — complete
- [x] Hashpath encode/decode — complete
- [x] Geohash, Plus Code, Maidenhead, GARS, GEOREF, DMS, NMEA, UTM import — complete
- [ ] WebAssembly / npm package
- [ ] Python package (PyPI)
- [ ] Swift package (iOS / macOS)
- [ ] Android library (JNI / NDK)
- [ ] QGIS plugin
- [ ] Web demo (hashsite.org)
- [ ] Test vector file (language-agnostic reference for port verification)
- [ ] MGRS / USNG import
- [ ] OS National Grid import
- [ ] Rumbleramble — haptic navigation mode (iOS)

---

→ **[Why Hashsite?](WHY.md)** — the case for open geocoding

→ **[License](LICENSE.md)** — HPL-2.0 terms
