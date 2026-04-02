![Hashsite banner](img/hashsitebanner.png)

**Open geocoding. Can be done with pencil and paper. Works offline. No API key. No rent. Locations that work for humans.**

A C library and coordinate format for encoding real-world locations as short, human-shareable alphadecimal strings. Compact, hierarchical, 3D-native, and free to implement.

| Code | Lat, Lon | Notes |
|---|---|---|
| `#7BA2` | 35.22°N, 101.76°W | Potter County, TX — 4-char, ~40km precision |
| `#7BA2CSoDZ` | 35.2220°N, 101.8310°W | Cadillac Ranch, Amarillo TX — 9-char, ~5m precision |
| `#7BA2CSoDZ^2` | 35.2220°N, 101.8310°W | Same, 2m above street level |
| `$FC64W` | 34.927°N, 101.663°W | From `#7BA2CSoDZ`: prefix = first 3 chars (`7BA`), nearest 8-char ending `FC64W` → `#7BAFC64W` (Palo Duro Canyon, 36km SE) |
| `#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2` | 33.628°N, 101.905°W | Hashpath: gate (33.628°N, 101.905°W) → code `4729#` → parking (33.629°N, 101.898°W) → stairs (33.629°N, 101.898°W) → door +2m (33.628°N, 101.899°W) |
| `#7B6.63IH.XB8` | 35.1240°N, 106.5692°W | Albuquerque — 10-char, ~1m precision, with checksum dots |

---

## Contents

- [Why Hashsite?](#why-hashsite)
- [Quick start](#quick-start)
- [The format](#the-format)
- [CLI reference](#cli-reference)
- [Library API](#library-api)
- [Coordinate import](#coordinate-import)
- [Roadmap](#roadmap)
- [W3WNKER](#w3wnker)
- [License](#license)

---

## Why Hashsite?

Communicating location is hard.

Say you've been in a traffic accident and there are injuries. You're on the phone with emergency services and they want to know where to send the ambulance.

Your phone knows exactly where you are. But you can't share your location over an emergency call once it's been connected.

Now imagine it's dark. Or snowing hard. Or you went through some trees, or down a ravine, or into a lake. Or all five at once. They need to know where you are to the nearest meter, not the nearest mile.

Launch Hashsite, and now you can read out the letters and numbers that will save your life.

The tools we currently have for communicating location are: street addresses, lat/lon strings, and a small collection of proprietary geocoding products that have done their best to lock that problem up behind a paywall and a terms of service. None of them solve it well.

### The failure of street addresses

A building address is a billing artifact designed for mail sorting. It does not tell you which entrance to use, where to park, which gate is the service gate, which of three buildings on a campus is the right one, or where the ambulance entrance is. It is not a usable delivery point, a usable pickup point, or a usable patient entrance. It is frequently not even accurate.

### The failure of lat/lon

Latitude and longitude are globally consistent and machine-readable. They are also verbose, non-hierarchical, easy to transpose, impossible to shorten meaningfully, and flat. Swapping two digits produces a different but plausible-looking location with no indication of error. Their precision is deceptive — most people have no intuition for what a difference of 0.001° means on the ground, so coordinates imply false exactness while simultaneously being impossible to sanity-check by eye. Reading `35.2220, -101.8310` aloud over a phone in a noisy environment or while injured is a meaningful failure mode.

### What3Words sucks — and why that matters

One company has raised over £150 million on the premise of assigning three random English words to every 3-meter cell on Earth and marketing it to emergency services.

It has also:

- Sent ambulances to the wrong location dozens of documented times due to structurally unavoidable confusable word pairs — a consequence of using a linear congruence generator to shuffle 57 trillion cells into a 40,000-word vocabulary, documented in peer-reviewed research
- Threatened the researchers who published that analysis
- Issued DMCA takedowns against open-source implementations
- Encrypted its wordlist inside a mobile app to prevent interoperability
- Convinced 85% of UK emergency services to depend on a system whose offline function requires payment and whose terms can change

That is not infrastructure. That is a hostage.

There is a long tradition of empires charging people for what they could make themselves — taxing salt, outlawing spinning wheels, requiring permits to collect rainwater. What3Words is that tradition applied to location data: a thing that costs nothing to produce, artificially enclosed, then rented back at a price set by the encloser. The Gandhi parallel is not an overstatement. Emergency services in Britain have been told they need a private company's permission slip to tell an ambulance where to go.

### What Hashsite does instead

**Offline-first.** The full codec is a single C file. No network, no API key, no server, no permission. Compile it and it works on anything.

**Hierarchical.** `#7B663I` is contained within `#7B663`. `#7B663` is contained within `#7B6`. Shorten a Hashsite to zoom out. Extend it to zoom in. Parent, child, and neighbor relationships are computable from the string itself.

**Compact.** Nine characters gives ~4m precision — fits in a text message, a QR code, a verbal exchange, a sticky note. No ambiguous characters: the only special case is that the letter O is always output as lowercase `o` to eliminate confusion with the digit 0.

**3D native.** Altitude is part of the format, not an afterthought. One character after `^` covers ±17m; four characters covers ±838km. Sub-meter precision available via precision mode.

**Path-aware.** A real arrival problem is a path problem, not a point problem. Hashpath encodes an ordered arrival sequence in a single compact string — full code for the first waypoint, differential encoding for each subsequent one, optional non-spatial labels for gate codes and PINs. This is the missing layer between raw coordinates and actual arrival.

**The confusable pair problem does not exist here.** Hashsite does not use words. The only ambiguity mitigation is `O` → `o`. Checksum dots catch transcription errors before they matter.

---

## Quick start

```bash
gcc -O2 hashsite.c -lm -o hashsite
./hashsite test          # verify your build
```

```bash
hashsite encode 35.222 -101.831 9     # -> #7BA2CSoDZ
hashsite decode 7BA2CSoDZ             # -> lat=35.222... lon=-101.831...
hashsite distance 7B663I 76B82D       # -> 2905.986 km
hashsite frommaidenhead FN31pr        # -> #7703K1QN
hashsite fromnmea '$GPGGA,...'        # -> hashsite + altitude from GPS device
```

---

## The format

### Basic structure

Every Hashsite begins with `#`. The character set is `0–9` and `A–Z`, with lowercase `o` substituted for uppercase `O` to eliminate the most common visual ambiguity with `0`. Input is case-insensitive.

### Precision

Each character subdivides the current cell by 6×6. Approximate equatorial precision:

| Characters | Cell size | Use |
|---|---:|---|
| 1 | 7000 km | Continental |
| 2 | 1200 km | Country |
| 3 | 200 km | Metro area |
| 4 | 40 km | City |
| 5 | 5 km | District |
| 6 | 1000 m | Neighborhood |
| 7 | 200 m | City block |
| 8 | 25 m | Building entrance |
| 9 | 5 m | Person-scale |
| 10 | 1 m | Sub-meter |

Cells narrow toward the poles. Use `hashsite precision N lat` for latitude-aware dimensions.

The number of characters encodes the desired precision tolerance, not the precision of the input coordinates. A GPS fix at 7-decimal-place accuracy encoded as 7 characters gives ~143m output precision. The extra input precision is discarded — intentionally.

### Grid structure

The first character divides the globe into 36 zones: 6 longitude bands × 6 latitude bands. The latitude bands use equal-area boundaries at 0°, ±19.47° (= arcsin(1/3)), and ±41.81°, keeping cells more equal in area than a naive rectangular grid.

The second character subdivides each first-character zone into 36 cells using a **9×4 grid** — 9 longitude columns × 4 latitude rows — for all non-polar zones. Polar zones (above ±41.81°) use a variable column count per latitude row (1/1/2/3/3/4/5/5/6/6, from pole to band edge), which reduces the extreme east-west crowding that afflicts rectangular grids at high latitudes. All characters after the second use regular **6×6** subdivision.


### Hierarchy

Hashsite is prefix-hierarchical:
- `#7B663I` is contained within `#7B663`
- `#7B663` is contained within `#7B6`
- Prefixes always contain their extensions

Parent, child, and neighbor relationships are all computable without external data.

### Checksum dots

Hashsite supports optional checksum dots:

```
#7B6.63IH.XB8
```

The dots are placed deterministically from the string content — not arbitrarily. A dotted Hashsite describes the same location as the undotted one. The Luhn checksum is computed over the **full string including altitude**, so the same horizontal code with different altitude produces different dot positions. Use dots when the code will be transcribed by hand, read aloud, or relayed in conditions where a wrong digit could matter.

### Altitude

Append altitude after `#CODE` using `^`:

```
#7BA2CSoDZ^1       +1 m above street level
#7BA2CSoDZ^S       −10 m below street level
#7BA2CSoDZ^I1I     +1.5 m above street level
#7BA2CSoDZ^255T    +100001 m above street level
```

**Coarse mode** — first character after `^` is signed base-36:

| Character | Value |
|---|---|
| `0` | 0 m |
| `1`–`H` | +1 to +17 m |
| `J`–`Z` | −1 to −17 m |
| `I` | switch to precision mode |

Big-endian — most significant digit first. 1 char: ±17m, 2 chars: ±647m, 3 chars: ±23km, 4 chars: ±838km.

**Precision mode** — begins with `^I`. First char after `I` = signed integer meters. Subsequent chars fractional (÷36 each). `I` as first-after-`I` = negative sub-meter zero.

```
^I1I   = +1.5 m      ^IJI   = −1.5 m
^I00CYK5R ≈ +0.01 m
```

### Hashpath

An ordered arrival sequence. All waypoints normalize to the same precision. The first waypoint is a full code; each subsequent waypoint encodes only the characters that differ from the previous one. Single lowercase letter labels precede each differential segment. `c` is reserved for non-spatial data (gate codes, door PINs) and is never a mappable location.

```
#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2
```

A trailer park in Lubbock, TX — multiple buildings, no sane addressing. Breaking it down:

| Segment | Label | Meaning | Full code |
|---|---|---|---|
| `#7BGPSDMUT` | *(none)* | Gate — first waypoint, full 9-char code, always unlabelled | `#7BGPSDMUT` |
| `c4729#` | `c` (code) | Gate PIN — non-spatial, not a location | — |
| `pFCDC` | `p` (parking) | Shares first 5 chars with gate; only `FCDC` differs | `#7BGPSFCDC` |
| `sEN4L` | `s` (stairs) | Shares first 5 chars with parking; only `EN4L` differs | `#7BGPSEN4L` |
| `d1T^2` | `d` (door) | Shares first 7 chars with stairs; only `1T` differs, +2m altitude | `#7BGPSEN1T^2` |

The first waypoint is always a full unlabelled code. Each subsequent segment starts with a single lowercase label char followed by its differential suffix.

---

## CLI reference

Build: `gcc -O2 hashsite.c -lm -o hashsite`

### Encode / decode

```bash
hashsite encode 35.222 -101.831 9     # -> #7BA2CSoDZ
hashsite decode 7BA2CSoDZ             # lat, lon, and optionally altitude
hashsite bbox 7B663I                  # full bounding box and cell dimensions
```

### Inspection

```bash
hashsite valid 7B663IHXB8             # exits 0 if valid
hashsite precision 9                  # ~4m equatorial
hashsite precision 9 35.0             # latitude-aware: height × width
hashsite parent 7B663IHXB8            # -> #7B663IHX
hashsite contains 7B663 7B663IHXB8    # exits 0 (yes)
```

### Altitude

```bash
hashsite altencode 10                 # -> ^A
hashsite altencode 1.5                # -> ^I1I  (auto precision mode)
hashsite altencode 100001             # -> ^255T
hashsite altencode -10                # -> ^S
hashsite altdecode "^I1I"             # -> 1.5000000 m
```

### Geometry — 2D

```bash
hashsite distance 7B663I 76B82D       # -> 2905.986 km
hashsite bearing 7B663I 76B82D        # -> 67.86 degrees (ENE)
hashsite midpoint 7B663I 76B82D       # -> #74EVoC
hashsite offset 7B663IHXB8 100 50     # translate 100m N, 50m E
hashsite neighbors 7B663I             # up to 8 adjacent cells
hashsite children 7B663I              # all 36 sub-cells
```

### Geometry — 3D

```bash
hashsite distance3d 7B663I 0 76B82D 1000    # 3D distance with altitude
hashsite midpoint3d 7B663I 0 76B82D 200     # -> #74EVoC^2S  (100m altitude)
hashsite offset3d 7B663IHXB8 10 0 50 5      # translate east and up
```

### Dots

```bash
hashsite luhn 7B663IHXB8              # -> #7B6.63IH.XB8
hashsite luhn 7B663IHXB8^A            # different dots — altitude is part of checksum
hashsite luhncheck "7B6.63IH.XB8^A"   # exits 0 if dots match (with altitude)
hashsite luhncheck 7B6.63IH.XB8       # exits 1 — dots were computed without ^A
```

### Pattern matching

`closest` finds the geographically nearest Hashsite matching a suffix pattern.

| Pattern | Prefix used | Result length |
|---|---|---|
| `$SUFFIX` | first 3 chars of your position | 3 + len(SUFFIX) |
| `%SUFFIX` | first 5 chars of your position | 5 + len(SUFFIX) |
| `SUFFIX` | none (fixed location) | len(SUFFIX) |

Your position length doesn't affect the result length — only the prefix length (3 or 5) and suffix length matter. The nearest match is found geographically — the result may use a different prefix than your own. `$FC64W` from `#7BA2CSoDZ` gives `#7BAFC64W` (Palo Duro Canyon, 36km SE).

```bash
hashsite closest 7BA2CSoDZ '$FC64W'  # prefix=7BA -> nearest 8-char ending FC64W -> #7BAFC64W
hashsite closest 7BA2CSoDZ '%Y2'     # prefix=7BA2C -> nearest 7-char ending Y2 -> #7BA2CY2
hashsite closest 7B663IHXB8 '$XB8'  # prefix=7B6 -> nearest 6-char ending XB8 -> #7A5XB8
hashsite closest 62AZZ492 '$00009'  # prefix=62A -> nearest 8-char ending 00009 -> #62B00009
```

#### Cross-zone example: Chicago

A club in Brighton Park (41.801°N, 87.625°W) texts its location as `$04H49` — a 5-character suffix that resolves to a full 8-char building-entrance-precision code (3-char prefix from your position + 5-char suffix). You're in a Bridgeport apartment (`#1XVWQNK82`, 41.842°N, 87.644°W), just north of the 41.81° polar band boundary. The club is just south of it. The two locations are in different Hashsite latitude bands — `#1X...` polar, `#74...` mid-latitude — and share no prefix characters at all.

```bash
hashsite closest 1XVWQNK82 '$04H49'
# -> #74504H49   (41.801°N, 87.625°W — building entrance precision, correct)
```

A naive substitution of your first 3 chars gives `#1XV04H49` — which decodes to 42.61°N, 88.10°W, nearly 100km away in Wisconsin. The geographic search correctly crosses the band boundary regardless.

---

## Coordinate import

All `from*` commands accept an optional `nchars` argument for output precision.

```bash
# Geocode systems
hashsite fromgeohash 9q8yy 9
hashsite frompluscode 9C3X+GV5C 9
hashsite frommaidenhead FN31pr          # ham radio grid square
hashsite fromgars 147LL                 # DoD / Civil Air Patrol
hashsite fromgeoref MK1406              # aviation / NATO

# Surveyor and GPS formats
hashsite fromdms "40d42m51sN" "-74.0060"
hashsite fromdms "40°42'51\"N" "74°0'21\"W"
hashsite fromnmea '$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18'
hashsite fromutm "18T 583960 4507523"   # spherical approximation, ~50m
```

Supported: Geohash, Plus Code (OLC), Maidenhead, GARS, GEOREF, DMS, DDM, NMEA GGA, NMEA RMC, UTM.

---

## Library API

Include `hashsite.h`, link with `hashsite.c -lm`.

### Core

```c
void   ll2hsps    (double lat, double lon, int nchars, char *buf);
int    hsps2ll    (const char *hs, double *lat_out, double *lon_out);
int    hsps2bbox  (const char *hs, hs_bbox *bbox);
```

### Inspection

```c
int    hs_clean       (const char *in, char *buf);
int    hs_valid       (const char *in);
double hs_precision_m (int nchars);
void   hs_precision_at(double lat_deg, int nchars, double *hgt_m, double *wid_m);
int    hs_parent      (const char *in, char *out);
int    hs_contains    (const char *a, const char *b);
```

### Altitude

```c
#define HS_ALT_NONE   (1e308)   /* sentinel: no altitude */
#define HS_ALT_MAXLEN 16

int    hs_alt_encode     (double meters, int precision, char *out);
double hs_alt_decode     (const char *s);
int    hs_alt_encode_auto(double meters, char *out);
```

### Geometry — 2D

```c
double hs_distance_m   (const char *a, const char *b);
double hs_bearing      (const char *a, const char *b);
int    hs_midpoint     (const char *a, const char *b, char *out);
int    hs_offset       (const char *in, double north_m, double east_m, char *out);
int    hs_neighbors    (const char *in, char neighbors[][HS_MAXLEN + 1]);
int    hs_children     (const char *in, char children[][HS_MAXLEN + 1]);
int    hs_guess_closest(const char *user_hs, const char *pattern, char *result);
```

### Geometry — 3D

```c
double hs_distance3d_m (const char *a, double a_alt, const char *b, double b_alt);
int    hs_offset3d     (const char *in, double in_alt,
                        double north_m, double east_m, double up_m,
                        char *out, double *out_alt);
int    hs_midpoint3d   (const char *a, double a_alt, const char *b, double b_alt,
                        char *out, double *out_alt);
```

### Paths

```c
typedef struct {
    double lat, lon, alt_m;         /* alt_m = HS_ALT_NONE if absent */
    char   code[HS_MAXLEN + 1];
    int    nchars;
} hs_waypoint;

void hs_encode_path(hs_waypoint *wps, int nwps, int nchars_each, char *buf);
int  hs_decode_path(const char *in, hs_waypoint *wps, int max_wps);
```

### Dots

```c
int hs_luhn_place(const char *in, char *out);   /* out: HS_MAXLEN + HS_ALT_MAXLEN + 3 */
int hs_luhn_check(const char *in);
```

### Import wrappers

```c
int hs_from_geohash   (const char *geohash,  int nchars, char *out);
int hs_from_pluscode  (const char *pluscode, int nchars, char *out);
int hs_from_maidenhead(const char *loc,      int nchars, char *out);
int hs_from_gars      (const char *gars,     int nchars, char *out);
int hs_from_georef    (const char *gr,       int nchars, char *out);
int hs_from_dms       (const char *lat_s, const char *lon_s, int nchars, char *out);
int hs_from_nmea_gga  (const char *sentence, int nchars, char *out, double *alt_out);
int hs_from_nmea_rmc  (const char *sentence, int nchars, char *out);
int hs_from_utm       (const char *s,        int nchars, char *out);
```

All `nchars <= 0` selects precision automatically from the source format.

---

## Roadmap

- [x] C library and CLI
- [x] 2D and 3D geometry
- [x] Altitude encoding (coarse and precision modes)
- [x] Checksum dot placement and verification (Luhn-derived, includes vertical component)
- [x] Hashpath encode/decode
- [x] Geohash, Plus Code, Maidenhead, GARS, GEOREF, DMS, NMEA, UTM import
- [ ] WebAssembly / npm package
- [ ] Python package (PyPI)
- [ ] Swift package (iOS / macOS)
- [ ] Android library (JNI / NDK)
- [ ] QGIS plugin
- [ ] Web demo (hashsite.org)
- [ ] MGRS / USNG import (requires ellipsoidal TM math)
- [ ] OS National Grid import
- [ ] Rumbleramble — haptic navigation mode

---

## W3WNKER

**W3WNKER** (Worldwide 3D Wayfinding: iNteroperability Kernel for Emergency Response) is a companion project providing an offline, open codec for W3W-compatible addresses.

Free license: $0. Commercial license: $6,969.69. Retroactive scofflaw amnesty: $1.00. All licenses identical in all respects.

---

## License

**Hashsite Public License v2.0 (HPL-2.0).** Not MIT. Not OSI open source.

Free for personal use, academic use, non-commercial open-source projects, journalism, and small commercial use (under 10 employees and $1M annual revenue).

A paid license is required for governments, militaries, intelligence agencies, law enforcement, large enterprises, and contractors acting on their behalf. **Developer Welcome Kit: $999** — 3-year term, up to 5 developers, one product.

See `LICENSE` for full terms. Licensing contact: **licensing@hashsite.org**

---

**Matt Channon** · [hashsite.org](https://hashsite.org)
