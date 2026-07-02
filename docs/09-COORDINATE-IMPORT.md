# 9. Coordinate import and interoperability

[README](../README.md) | Prev: [8. Library API](08-LIBRARY-API.md) | Next: [10. Web app behavior](10-WEB-APP.md)

---

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

---

[README](../README.md) | Prev: [8. Library API](08-LIBRARY-API.md) | Next: [10. Web app behavior](10-WEB-APP.md)
