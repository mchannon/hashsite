# 2. Code format, alphabet, precision, and rubric

[README](../README.md) | Prev: [1. What is a Hashsite?](01-WHAT-IS-A-HASHSITE.md) | Next: [3. Grid and encoding model](03-GRID-AND-ENCODING.md)

---

This is the core Hashsite material.

A Hashsite is a compact spatial code, not a random shortlink.

Examples:

```text
#7BA2
#7BA2CSoDZ
#7BA2CSoDZ^2
#7B6.63IH.XB8
```

## Character set

Hashsite uses a 36-symbol alphadecimal character set:

```text
0-9
A-Z
```

The canonical display is uppercase-oriented, with one practical exception: lowercase `o` may be used for `O` to reduce `O/0` ambiguity.

Input is case-insensitive.

## Visual markers

Common forms:

```text
#CODE
#CODE^
#C.OD.E
#CODE^ALT
```

- `#` visually marks a Hashsite.
- `^` terminates the horizontal code and/or introduces altitude.
- Dots are optional readability/checksum helpers.
- Altitude follows `^`.

## Precision by length

Approximate equatorial precision:

| Characters | Cell size | Use |
|---|---:|---|
| 1 | ~7000 km | Continental |
| 2 | ~1200 km | Country / large region |
| 3 | ~200 km | Metro / regional |
| 4 | ~40 km | City-scale |
| 5 | ~5 km | District |
| 6 | ~1000 m | Neighborhood |
| 7 | ~200 m | Block |
| 8 | ~25 m | Building / entrance |
| 9 | ~5 m | Person-scale |
| 10 | ~1 m | Sub-meter / high precision |

The number of characters expresses the chosen output precision. Extra GPS decimal places are intentionally discarded when encoding to a shorter Hashsite.

## Rubric

Use fewer characters when the area is all that matters. Use more characters when the exact point matters.

Examples:

- 4 characters: city/general area
- 6 characters: neighborhood
- 8 characters: property, entrance, trailhead
- 9 characters: person-scale point, delivery, gate, pickup
- 10 characters: sub-meter or inspection/survey use

## Hierarchy

Hashsite is prefix-hierarchical.

```text
#7B663I is inside #7B663
#7B663 is inside #7B6
```

Removing characters zooms out. Adding characters zooms in.

---

[README](../README.md) | Prev: [1. What is a Hashsite?](01-WHAT-IS-A-HASHSITE.md) | Next: [3. Grid and encoding model](03-GRID-AND-ENCODING.md)
