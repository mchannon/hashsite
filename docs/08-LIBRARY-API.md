# 8. Library API

[README](../README.md) | Prev: [7. CLI reference with outputs](07-CLI-REFERENCE.md) | Next: [9. Coordinate import with outputs](09-COORDINATE-IMPORT.md)

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
void   ll2hsps    (double lat, double lon, int nchars, char *buf);
int    hsps2ll    (const char *hs, double *lat_out, double *lon_out);
int    hsps2bbox  (const char *hs, hs_bbox *bbox);
```

## Inspection

```c
int    hs_clean       (const char *in, char *buf);
int    hs_valid       (const char *in);
double hs_precision_m (int nchars);
void   hs_precision_at(double lat_deg, int nchars, double *hgt_m, double *wid_m);
int    hs_parent      (const char *in, char *out);
int    hs_contains    (const char *a, const char *b);
```

## Altitude

```c
#define HS_ALT_NONE   (1e308)
#define HS_ALT_MAXLEN 16

int    hs_alt_encode     (double meters, int precision, char *out);
double hs_alt_decode     (const char *s);
int    hs_alt_encode_auto(double meters, char *out);
```

## Geometry — 2D

```c
double hs_distance_m   (const char *a, const char *b);
double hs_bearing      (const char *a, const char *b);
int    hs_midpoint     (const char *a, const char *b, char *out);
int    hs_offset       (const char *in, double north_m, double east_m, char *out);
int    hs_neighbors    (const char *in, char neighbors[][HS_MAXLEN + 1]);
int    hs_children     (const char *in, char children[][HS_MAXLEN + 1]);
int    hs_guess_closest(const char *user_hs, const char *pattern, char *result);
```

## Geometry — 3D

```c
double hs_distance3d_m (const char *a, double a_alt, const char *b, double b_alt);
int    hs_offset3d     (const char *in, double in_alt,
                        double north_m, double east_m, double up_m,
                        char *out, double *out_alt);
int    hs_midpoint3d   (const char *a, double a_alt, const char *b, double b_alt,
                        char *out, double *out_alt);
```

## Paths

```c
typedef struct {
    double lat, lon, alt_m;         /* alt_m = HS_ALT_NONE if absent */
    char   code[HS_MAXLEN + 1];
    int    nchars;
} hs_waypoint;

void hs_encode_path(hs_waypoint *wps, int nwps, int nchars_each, char *buf);
int  hs_decode_path(const char *in, hs_waypoint *wps, int max_wps);
```

## Dots

```c
int hs_luhn_place(const char *in, char *out);
int hs_luhn_check(const char *in);
```

## Import wrappers

```c
int hs_from_geohash   (const char *geohash,  int nchars, char *out);
int hs_from_pluscode  (const char *pluscode, int nchars, char *out);
int hs_from_maidenhead(const char *loc,      int nchars, char *out);
int hs_from_gars      (const char *gars,     int nchars, char *out);
int hs_from_georef    (const char *gr,       int nchars, char *out);
int hs_from_dms       (const char *lat_s, const char *lon_s, int nchars, char *out);
int hs_from_nmea_gga  (const char *sentence, int nchars, char *out, double *alt_out);
int hs_from_nmea_rmc  (const char *sentence, int nchars, char *out);
int hs_from_utm       (const char *s,        int nchars, char *out);
```

All `nchars <= 0` selects precision automatically from the source format.

---

[README](../README.md) | Prev: [7. CLI reference with outputs](07-CLI-REFERENCE.md) | Next: [9. Coordinate import with outputs](09-COORDINATE-IMPORT.md)
