# Grid and encoding model

Hashsite begins with global spatial subdivision and then refines the current cell.

## First character

The first character divides the globe into 36 zones: 6 longitude bands × 6 latitude bands.

The latitude bands use equal-area-ish boundaries at:

```text
0°
±19.47°
±41.81°
```

## Second character

The second character subdivides each first-character zone.

For tropical and mid-latitude zones, Hashsite uses a 9×4 grid.

For polar zones, it uses a variable row/column strategy to avoid absurdly narrow longitude cells near the poles.

## Third and later characters

From the third character onward, Hashsite uses regular 6×6 subdivision.

Each new character divides the current cell into 36 children.
