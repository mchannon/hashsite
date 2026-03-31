![Hashsite banner](img/hashsitebanner.png)

# Hashsite

**Open-source fractal geocoding library and coordinate format**

Hashsite encodes real-world locations as short, human-shareable **alphadecimal** strings using a **36-symbol** character set and a geometry designed to stay compact, hierarchical, and useful across the whole planet.

Examples:

- `#7BA2CSoDZ^`
- `7B663IHXB8`
- `#F.6NZ^J`
- `#WP1#WP2#WP3`

Hashsite is meant to be:

- **short**
- **offline**
- **hierarchical**
- **machine-friendly**
- **human-readable**
- **usable in 2D and 3D**
- **open-source from the start**

---

## Why Hashsite exists

Most location formats force an ugly tradeoff between one or more of these:

- short but opaque
- readable but verbose
- precise but not hierarchical
- global but awkward near the poles
- proprietary when they should not be

Hashsite takes a different route:

- a compact **base-36 alphadecimal** code
- a **fractal grid**
- equal-area-ish first-level world slicing
- a latitude-aware second-level subdivision
- simple 6×6 subdivision after that
- optional altitude
- optional readability dots
- optional multi-waypoint paths

The result is a code you can shorten, extend, compare by prefix, and manipulate without a cloud API.

---

## The basic idea

Hashsite starts with a **6×6 global grid**.

Each additional character subdivides the current region again.

- First character: global zone
- Second character: latitude-aware subdivision
- Third and later characters: regular **6×6** refinement

This makes Hashsite:

- **hierarchical** — prefixes contain suffixes
- **zoomable** — more characters means finer precision
- **locality-aware** — nearby places tend to share prefixes
- **easy to reason about** — parent/child relationships are obvious

You can think of a Hashsite as the center of a grid cell. If one character is enough for your use case, use one. If you need doorstep precision, use more.

---

## Precision

Approximate **equatorial** precision:

| Length | Cell size |
|---|---:|
| 1 | ~6679 km |
| 2 | ~1113 km |
| 3 | ~186 km |
| 4 | ~31 km |
| 5 | ~5 km |
| 6 | ~859 m |
| 7 | ~143 m |
| 8 | ~24 m |
| 9 | ~4 m |
| 10 | ~0.7 m |

Use latitude-aware sizing when exact east-west cell width matters; cells narrow toward the poles.

In practical terms:

- 6 chars: neighborhood scale
- 7 chars: block scale
- 8 chars: property / entrance scale
- 9 chars: near-human-position scale
- 10 chars: sub-meter scale

---

## Character set

Hashsite uses:

- `0-9`
- `A-Z`

with a practical display tweak:

- lowercase `o` may be used in place of uppercase `O` to reduce `O/0` ambiguity
- input is case-insensitive
- canonical display is uppercase-oriented alphadecimal styling

This gives you the full 36-symbol alphabet needed for compact codes without throwing away useful characters.

---

## Format

Canonical forms supported by the library include:

- `#<CODE>^`
- `<CODE>`
- `#<C.OD.E>^`
- `#<CODE>^<ALT>`
- `#WP1#WP2#WP3`

Where:

- `#` is an optional visual marker that says “this is a Hashsite”
- `^` is an optional terminator / altitude separator
- dots are optional readability helpers
- altitude comes after `^`
- multiple `#...` sequences can be concatenated as a **hashpath**

---

## Dots and readability

Some characters can still be visually confused in the wild, especially in screenshots, tweets, text messages, or verbally transcribed notes.

Hashsite supports **Luhn-derived dot placement**:

- dots are optional
- dots are derived from the content, not arbitrarily placed
- dotted strings remain the same location
- the library can place and verify them

Example:

- bare: `7B663IHXB8`
- dotted: `7B6.63IH.XB8`

This gives you a lightweight visual checksum and makes codes easier to read aloud or spot-check.

---

## Altitude

Hashsite is not limited to flat maps.

Altitude is encoded **after `^`**.

Examples:

- `#F6NZ^` — location only
- `#F6NZ^1` — one meter above street level
- `#F6NZ^J` — one meter below street level

The current library supports two altitude modes:

### Coarse mode
Compact integer-meter encoding in signed base-36 style.

Good for:
- floors
- rooftops
- basements
- parking structures
- trail elevation offsets
- ordinary navigation

### Precision mode
A higher-precision altitude form for sub-meter values.

Good for:
- surveying
- robotics
- drone / sensor work
- exact vertical offsets

The library also supports decoding altitude back to meters and auto-selecting an encoding mode.

---

## Hashpaths

Hashsite can represent **multiple waypoints in one string**.

Example idea:

- `#START#MID#END`
- or with altitude-bearing waypoints embedded

This is useful for:

- route fragments
- treasure hunts
- delivery legs
- survey chains
- game maps
- indoor-outdoor transitions
- “meet here, then go there” workflows

Hashpaths are first-class in the library, not an afterthought.

---

## What the library does

Hashsite is no longer just a format description. It is a real C library with a usable CLI.

### Core encode/decode
- latitude/longitude → Hashsite
- Hashsite → centroid lat/lon
- Hashsite → bounding box

### Inspection
- clean / strip decorated input
- validate a Hashsite
- compute approximate precision by length
- compute latitude-aware cell dimensions
- get parent cell
- test prefix containment

### 2D geometry
- distance
- bearing
- midpoint
- metric offset
- neighbors
- child cells

### 3D geometry
- 3D distance with altitude
- 3D offset
- 3D midpoint

### Path helpers
- encode hashpaths
- decode hashpaths

### Dot helpers
- place Luhn-derived dots
- verify dot placement

### Pattern / suffix matching
- find the nearest Hashsite matching a suffix pattern

### Import from other systems
- Geohash → Hashsite
- Plus Code → Hashsite

This makes Hashsite useful as both:
- a native coordinate system
- an interoperability layer

---

## CLI examples

A few examples from the current tool surface:

```bash
encode 35.222 -101.831 9
decode 7BA2CSoDZ
bbox 7B663I
distance 7B663I 76B82D
bearing 7B663I 76B82D
midpoint 7B663I 76B82D
offset 7B663IHXB8 100 50
luhn 7B663IHXB8
luhncheck 7B6.63IH.XB8
closest 7B663IHXB8 '$XB8'
fromgeohash 9q8yy 9
frompluscode 9C3X+GV5C 9
```

What these do:

- `encode` — turn coordinates into a Hashsite
- `decode` — recover centroid coordinates
- `bbox` — show full cell bounds
- `distance` — centroid-to-centroid great-circle distance
- `bearing` — compass bearing
- `midpoint` — cell halfway between two codes
- `offset` — translate a Hashsite by meters north/east
- `luhn` / `luhncheck` — readability dot support
- `closest` — nearest matching suffix pattern
- `fromgeohash` / `frompluscode` — import competing formats

---

## Hierarchy: parents, children, neighbors

Because Hashsite is prefix-based, it has a clean geometric family tree.

### Parent
Removing one character gives the containing larger region.

### Children
Adding one character yields one of the 36 sub-cells.

### Neighbors
The library can enumerate up to 8 adjacent cells at the same precision.

This matters because it makes the format usable for:

- tiling
- search windows
- map sampling
- adjacency logic
- local routing
- radius approximations
- “give me the next cell over” UX

---

## Pattern matching and suffixes

Hashsite includes a `closest` helper that can search for the nearest code matching a suffix pattern.

Pattern forms include:

- `$SUFFIX` — auto-prefix based on your current precision
- `$$$SUFFIX` — explicit shorter prefix behavior
- `SUFFIX` — fixed location pattern

This is useful for:
- vanity locations
- memorable endpoints
- scavenger hunts
- location branding
- human-friendly short endings near a real place

---

## Design notes

### 1) Fractal by default
Hashsite is meant to be shortened and extended naturally.

### 2) Offline matters
The format should be encodable and decodable without permission from anybody.

### 3) Human readability still matters
That is why dotted forms, optional markers, and a consistent character set exist.

### 4) 3D should not be bolted on later
Altitude belongs in the format family.

### 5) Interoperability is practical
Hashsite can import other coordinate formats instead of pretending they do not exist.

---

## Interop and companion work

Hashsite is the native format.

Companion tooling can sit beside it for interoperability, translation, migration, or critique of proprietary systems.

One proposed companion is **W3WNKER**:

> **Worldwide 3D Wayfinding: iNteroperability Kernel for Emergency Response**

That name is intentionally half-serious and half-provocative. Its purpose is straightforward: provide an offline, open interoperability layer so users are not trapped in a proprietary word-based location ecosystem.

Hashsite should remain the center of gravity. Interop tools should help people move **into** open geocoding, not deepen dependence on closed systems.

---

## Build philosophy

Hashsite is written in plain C with a small, readable public API.

The project aims for:

- low dependency count
- auditability
- embeddability
- portability
- library-first design
- CLI visibility for testing and demos

This makes it suitable for:

- servers
- command-line utilities
- embedded systems
- mobile wrappers
- mapping tools
- disaster-response workflows
- offline field software

---

## Why not just use latitude/longitude?

Latitude and longitude are universal, but not always convenient.

Hashsite gives you:

- a shorter shareable handle
- hierarchical prefixes
- adjustable precision
- optional altitude
- optional readability decoration
- path composition
- compact local geometry helpers

Lat/lon is still underneath. Hashsite is a friendlier wrapper for many human and software workflows.

---

## Status

Hashsite today is:

- a coordinate format
- a C library
- a CLI tool
- a 2D/3D geometry helper
- a path container
- a check-digit-style readability system
- an import target from other geocoders

The old README mostly described the philosophy.

The project now deserves documentation that treats it as a working geospatial toolkit.

---

## License

**Hashsite Public License v2.0**

See `LICENSE`.

---

## Author

**Matt Channon**

If you are here because you want a geocoder that is compact, hierarchical, offline-capable, and not dependent on someone else’s rent-seeking API, that is the point.
