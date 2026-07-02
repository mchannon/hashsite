# 7. CLI reference with outputs

[README](../README.md) | Prev: [6. Hashpaths](06-HASHPATHS.md) | Next: [8. Library API](08-LIBRARY-API.md)

---

Build:

```bash
gcc -O2 hashsite.c -lm -o hashsite
```

## Quick start

```bash
./hashsite test
# -> runs the test suite
```

## Encode / decode

```bash
hashsite encode 35.222 -101.831 9
# -> #7BA2CSoDZ

hashsite decode 7BA2CSoDZ
# -> lat=35.222... lon=-101.831...

hashsite bbox 7B663I
# -> full bounding box, centroid, and cell dimensions
```

## Inspection

```bash
hashsite valid 7B663IHXB8
# -> exits 0 if valid

hashsite precision 9
# -> ~4m equatorial / person-scale

hashsite precision 9 35.0
# -> latitude-aware height × width

hashsite parent 7B663IHXB8
# -> #7B663IHX

hashsite contains 7B663 7B663IHXB8
# -> exits 0 / yes
```

## Altitude

```bash
hashsite altencode 10
# -> ^A

hashsite altencode 1.5
# -> ^I1I

hashsite altencode 100001
# -> ^255T

hashsite altencode -10
# -> ^S

hashsite altdecode "^I1I"
# -> 1.5000000 m
```

## Geometry — 2D

```bash
hashsite distance 7B663I 76B82D
# -> 2905.986 km

hashsite bearing 7B663I 76B82D
# -> 67.86 degrees (ENE)

hashsite midpoint 7B663I 76B82D
# -> #74EVoC

hashsite offset 7B663IHXB8 100 50
# -> translates 100m north, 50m east

hashsite neighbors 7B663I
# -> up to 8 adjacent cells

hashsite children 7B663I
# -> all 36 sub-cells
```

## Geometry — 3D

```bash
hashsite distance3d 7B663I 0 76B82D 1000
# -> 3D distance including altitude

hashsite midpoint3d 7B663I 0 76B82D 200
# -> #74EVoC^2S  (100m altitude)

hashsite offset3d 7B663IHXB8 10 0 50 5
# -> translate east and up
```

## Dots

```bash
hashsite luhn 7B663IHXB8
# -> #7B6.63IH.XB8

hashsite luhn 7B663IHXB8^A
# -> different dots, because altitude is part of checksum

hashsite luhncheck "7B6.63IH.XB8^A"
# -> exits 0 if dots match with altitude

hashsite luhncheck 7B6.63IH.XB8
# -> exits 1 if dots were computed for a different full string
```

## Pattern matching

```bash
hashsite closest 7BA2CSoDZ '$FC64W'
# -> #7BAFC64W

hashsite closest 7BA2CSoDZ '%Y2'
# -> #7BA2CY2

hashsite closest 7B663IHXB8 '$XB8'
# -> #7A5XB8

hashsite closest 62AZZ492 '$00009'
# -> #62B00009
```

---

[README](../README.md) | Prev: [6. Hashpaths](06-HASHPATHS.md) | Next: [8. Library API](08-LIBRARY-API.md)
