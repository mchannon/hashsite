# 4. Altitude and 3D

[README](../README.md) | Prev: [3. Grid structure and hierarchy](03-GRID-STRUCTURE.md) | Next: [5. Readability, checksums, and dots](05-READABILITY-CHECKSUMS-DOTS.md)

---

Hashsite is 3D-native.

Append altitude after the horizontal code using `^`.

```text
#7BA2CSoDZ^1       +1 m above street level
#7BA2CSoDZ^S       −10 m below street level
#7BA2CSoDZ^I1I     +1.5 m above street level
#7BA2CSoDZ^255T    +100001 m above street level
```

## Coarse mode

The first character after `^` is signed base-36.

| Character | Value |
|---|---|
| `0` | 0 m |
| `1`–`H` | +1 to +17 m |
| `J`–`Z` | −1 to −17 m |
| `I` | switch to precision mode |

Big-endian: most significant digit first.

Approximate coverage:

- 1 char: ±17m
- 2 chars: ±647m
- 3 chars: ±23km
- 4 chars: ±838km

This covers common wayfinding situations such as floors, rooftops, basements, parking decks, bridges, and tunnels.

## Precision mode

Precision mode begins with `^I`.

Examples:

```text
^I1I   = +1.5 m
^IJI   = −1.5 m
^I00CYK5R ≈ +0.01 m
```

Precision mode exists for sub-meter vertical offsets, surveying, robotics, drones, sensors, and exact elevation work.

## Street level vs sea level

The oldest design notes also discussed relative-to-street-level and relative-to-sea-level forms using repeated carets.

That idea explains the design pressure: everyday users often care about “one floor above me” more than ellipsoid height, while survey/robotics users may care about absolute elevation.

The current library’s documented form is the signed altitude string after `^`, with coarse and precision modes.

---

[README](../README.md) | Prev: [3. Grid structure and hierarchy](03-GRID-STRUCTURE.md) | Next: [5. Readability, checksums, and dots](05-READABILITY-CHECKSUMS-DOTS.md)
