# 8. Library API

[README](../README.md) | Prev: [7. CLI reference](07-CLI-REFERENCE.md) | Next: [9. Coordinate import and interoperability](09-COORDINATE-IMPORT.md)

---

Include:

```c
#include "hashsite.h"
```

Link with:

```bash
hashsite.c -lm
```

## Core

```c
void ll2hsps(double lat, double lon, int nchars, char *buf);
int  hsps2ll(const char *hs, double *lat_out, double *lon_out);
int  hsps2bbox(const char *hs, hs_bbox *bbox);
```

## Inspection, geometry, altitude

See `hashsite.h` for exact current signatures for validation, precision, parent/child/neighbor, distance, bearing, midpoint, offset, altitude, and path helpers.

---

[README](../README.md) | Prev: [7. CLI reference](07-CLI-REFERENCE.md) | Next: [9. Coordinate import and interoperability](09-COORDINATE-IMPORT.md)
