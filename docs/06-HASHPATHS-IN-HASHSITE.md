# Hashpaths in the Hashsite library

Hashsite includes path-aware behavior.

A single Hashsite marks a point. A Hashpath can represent an ordered arrival sequence.

Example:

```text
#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2
```

| Segment | Meaning |
|---|---|
| `#7BGPSDMUT` | First waypoint, full code |
| `c4729#` | Non-spatial code payload |
| `pFCDC` | Parking waypoint by differential suffix |
| `sEN4L` | Stairs waypoint by differential suffix |
| `d1T^2` | Door waypoint, +2m altitude |

The first waypoint is full. Later spatial segments can encode only what differs from the previous point.

For the companion product and current procedural-direction docs, see Hashpath:

<https://hashpath.org>
