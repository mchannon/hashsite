# 6. Hashpaths

[README](../README.md) | Prev: [5. Readability, checksums, and dots](05-READABILITY-CHECKSUMS-DOTS.md) | Next: [7. CLI reference with outputs](07-CLI-REFERENCE.md)

---

A Hashpath is an ordered arrival sequence.

All waypoints normalize to the same precision.

The first waypoint is a full code. Each subsequent waypoint encodes only the characters that differ from the previous one.

Single lowercase letter labels precede each differential segment.

`c` is reserved for non-spatial data such as gate codes and door PINs. It is never a mappable location.

## Example

```text
#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2
```

A trailer park in Lubbock, TX. Buildings are unmarked and use a seemingly random numbering system. If you have delivered pizza, driven rideshare, or tried to get an ambulance to the right door, you know what pain this solves.

| Segment | Label | Meaning | Full code |
|---|---|---|---|
| `#7BGPSDMUT` | *(none)* | Gate — first waypoint, full 9-char code, always unlabelled | `#7BGPSDMUT` |
| `c4729#` | `c` (code) | Gate PIN — non-spatial, not a location | — |
| `pFCDC` | `p` (parking) | Shares first 5 chars with gate; only `FCDC` differs | `#7BGPSFCDC` |
| `sEN4L` | `s` (stairs) | Shares first 5 chars with parking; only `EN4L` differs | `#7BGPSEN4L` |
| `d1T^2` | `d` (door) | Shares first 7 chars with stairs; only `1T` differs, +2m altitude | `#7BGPSEN1T^2` |

The first waypoint is always a full unlabelled code. Each subsequent spatial segment starts with a lowercase label followed by its differential suffix.

Hashpath is now its own live companion product:

<https://hashpath.org>

---

[README](../README.md) | Prev: [5. Readability, checksums, and dots](05-READABILITY-CHECKSUMS-DOTS.md) | Next: [7. CLI reference with outputs](07-CLI-REFERENCE.md)
