# 3. Grid structure and hierarchy

[README](../README.md) | Prev: [2. Format, codes, and precision](02-FORMAT-CODES-PRECISION.md) | Next: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md)

---

## The 6×6 idea

Hashsite begins with a 6×6 alphadecimal grid.

Fill that grid with:

```text
0 1 2 3 4 5
6 7 8 9 A B
C D E F G H
I J K L M N
O P Q R S T
U V W X Y Z
```

That gives 36 choices per character.

## First character: global zone

The first character divides the globe into 36 zones:

```text
6 longitude bands × 6 latitude bands
```

The latitude bands use equal-area-ish boundaries at:

```text
0°
±19.47° = arcsin(1/3)
±41.81°
```

This keeps cells more equal in area than a naive Mercator-like rectangular grid.

## Why not naive Mercator?

A simple rectangular grid over a Mercator-like map overrepresents polar areas and underrepresents equatorial areas.

Hashsite uses latitude bands that split the Earth into six roughly equal-area slices, so the first character represents roughly comparable surface area wherever it appears.

## Second character

The second character subdivides each first-character zone into 36 cells.

For tropical and mid-latitude zones, Hashsite uses a 9×4 grid:

```text
9 longitude columns × 4 latitude rows
```

This produces cells that are more reasonably shaped than another 6×6 split at that level.

## Polar handling

In polar zones above ±41.81°, using 9×4 or 6×6 creates absurdly precise longitudes and imprecise latitudes.

So polar zones use a variable column-count strategy by row:

```text
1 / 1 / 2 / 3 / 3 / 4 / 5 / 5 / 6 / 6
```

from pole to band edge.

These do not look square in the projection, but they represent more similar real-world sizes.

## Third and later characters

From the third character onward, Hashsite uses regular 6×6 subdivision.

Each new character selects one of 36 child cells.

## Hierarchy

Hashsite is prefix-hierarchical:

```text
#7B663I is contained within #7B663
#7B663 is contained within #7B6
```

Shortening a Hashsite zooms out.

Extending a Hashsite zooms in.

Parent, child, and neighbor relationships are computable without external data.

---

[README](../README.md) | Prev: [2. Format, codes, and precision](02-FORMAT-CODES-PRECISION.md) | Next: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md)
