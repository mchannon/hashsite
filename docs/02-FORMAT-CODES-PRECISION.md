# 2. Format, codes, and precision rubric

[README](../README.md) | Prev: [1. Why Hashsite?](01-WHY-HASHSITE.md) | Next: [3. Grid structure and hierarchy](03-GRID-STRUCTURE.md)

---

## Basic structure

Every Hashsite begins with `#`.

The character set is:

```text
0–9
A–Z
```

with lowercase `o` substituted for uppercase `O` to reduce the most common visual ambiguity with `0`.

Input is case-insensitive.

## Examples

| Code | Lat, Lon | Notes |
|---|---|---|
| `#7BA2` | 35.22°N, 101.76°W | Potter County, TX — 4-char, ~40km precision |
| `#7BA2CSoDZ` | 35.2220°N, 101.8310°W | Cadillac Ranch, Amarillo TX — 9-char, ~5m precision |
| `#7BA2CSoDZ^2` | 35.2220°N, 101.8310°W | Same horizontal point, 2m above street level |
| `#7B6.63IH.XB8` | 35.1240°N, 106.5692°W | Albuquerque — 10-char, ~1m precision, with checksum dots |

## Precision

Each character subdivides the current cell. Approximate equatorial precision:

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

Cells narrow toward the poles. Use:

```bash
hashsite precision N lat
```

for latitude-aware dimensions.

## The precision rubric

The number of characters encodes the desired precision tolerance, not the precision of the input coordinates.

A GPS fix with many decimal places encoded as 7 characters gives roughly city-block precision. The extra input precision is discarded intentionally.

Use:

- 4 characters for city/general area
- 6 characters for neighborhood
- 8 characters for property, entrance, trailhead
- 9 characters for person-scale points, delivery, gate, pickup
- 10 characters for sub-meter or inspection/survey use

---

[README](../README.md) | Prev: [1. Why Hashsite?](01-WHY-HASHSITE.md) | Next: [3. Grid structure and hierarchy](03-GRID-STRUCTURE.md)
