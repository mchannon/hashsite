# 9. Coordinate import with outputs

[README](../README.md) | Prev: [8. Library API](08-LIBRARY-API.md) | Next: [10. Pattern matching and suffixes](10-PATTERN-MATCHING.md)

---

All `from*` commands accept an optional `nchars` argument for output precision.

## Geocoder systems

```bash
hashsite fromgeohash 9q8yy 9
# -> Hashsite at requested precision for the Geohash cell centroid

hashsite frompluscode 9C3X+GV5C 9
# -> Hashsite at requested precision for the Plus Code / OLC location

hashsite frommaidenhead FN31pr
# -> #7703K1QN
```

## DoD / aviation / rescue-style formats

```bash
hashsite fromgars 147LL
# -> Hashsite for the GARS area reference

hashsite fromgeoref MK1406
# -> Hashsite for the GEOREF location
```

## Surveyor and GPS formats

```bash
hashsite fromdms "40d42m51sN" "-74.0060"
# -> Hashsite for roughly New York / lower Manhattan area

hashsite fromdms "40°42'51\"N" "74°0'21\"W"
# -> Hashsite for the DMS coordinate pair

hashsite fromnmea '$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18'
# -> Hashsite plus altitude from the GPS sentence

hashsite fromutm "18T 583960 4507523"
# -> Hashsite from UTM, spherical approximation, about ~50m tolerance
```

Supported: Geohash, Plus Code / OLC, Maidenhead, GARS, GEOREF, DMS, DDM, NMEA GGA, NMEA RMC, and UTM.

## Notes on output

Some imports return exact-looking Hashsites from inherently coarse source systems.

The output precision should be understood as:

```text
source format precision × requested Hashsite precision
```

A coarse source converted to a long Hashsite does not magically create ground truth.

---

[README](../README.md) | Prev: [8. Library API](08-LIBRARY-API.md) | Next: [10. Pattern matching and suffixes](10-PATTERN-MATCHING.md)
