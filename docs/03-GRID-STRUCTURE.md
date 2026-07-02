# 3. Grid structure and hierarchy

[README](../README.md) | Prev: [2. Format, codes, and precision rubric](02-FORMAT-CODES-PRECISION.md) | Next: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md)

---

## First character

The first character divides the globe into 36 zones:

```text
6 longitude bands × 6 latitude bands
```

The latitude bands use equal-area boundaries at:

```text
0°
±19.47° = arcsin(1/3)
±41.81°
```

This keeps cells more equal in area than a naive rectangular grid.

## Second character

The second character subdivides each first-character zone into 36 cells.

For non-polar zones, this is a 9×4 grid:

```text
9 longitude columns × 4 latitude rows
```

For polar zones above ±41.81°, Hashsite uses variable column counts by row:

```text
1 / 1 / 2 / 3 / 3 / 4 / 5 / 5 / 6 / 6
```

from pole to band edge. This reduces extreme east-west crowding near the poles.

## Third and later characters

All characters after the second use regular 6×6 subdivision.

Each added character zooms into one of 36 child cells.

## Hierarchy

Hashsite is prefix-hierarchical:

```text
#7B663I is contained within #7B663
#7B663 is contained within #7B6
```

Prefixes always contain their extensions.

Parent, child, and neighbor relationships are computable without external data.

---

[README](../README.md) | Prev: [2. Format, codes, and precision rubric](02-FORMAT-CODES-PRECISION.md) | Next: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md)
