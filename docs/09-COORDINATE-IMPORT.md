# Coordinate import and interoperability

Hashsite can import other coordinate formats instead of pretending they do not exist.

Supported or planned import surfaces include:

- Geohash
- Plus Codes / OLC
- Maidenhead
- GARS
- GEOREF
- DMS
- DDM
- NMEA GGA
- NMEA RMC
- UTM

Examples:

```bash
hashsite fromgeohash 9q8yy 9
hashsite frompluscode 9C3X+GV5C 9
hashsite frommaidenhead FN31pr
hashsite fromnmea '$GPGGA,...'
```
