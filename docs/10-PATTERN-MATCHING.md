# 10. Pattern matching and suffixes

[README](../README.md) | Prev: [9. Coordinate import with outputs](09-COORDINATE-IMPORT.md) | Next: [11. Web app behavior](11-WEB-APP.md)

---

`closest` finds the geographically nearest Hashsite matching a suffix pattern.

## Pattern forms

| Pattern | Prefix used | Result length |
|---|---|---|
| `$SUFFIX` | first 3 chars of your position | 3 + len(SUFFIX) |
| `%SUFFIX` | first 5 chars of your position | 5 + len(SUFFIX) |
| `SUFFIX` | none | len(SUFFIX) |

Your position length does not determine the result length. The prefix rule and suffix length do.

## Examples

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

## Cross-zone example: Chicago

A club in Brighton Park texts:

```text
$04H49
```

You are in Bridgeport at:

```text
#1XVWQNK82
```

The two locations are in different Hashsite latitude bands and share no prefix characters.

```bash
hashsite closest 1XVWQNK82 '$04H49'
# -> #74504H49
```

A naive substitution of your first 3 chars would produce a wrong Wisconsin-ish answer. Geographic search correctly crosses the band boundary.

## Uses

Pattern matching can support:

- vanity locations
- memorable suffixes
- scavenger hunts
- place branding
- human-friendly short endings near real places
- puzzle/game/tour workflows

---

[README](../README.md) | Prev: [9. Coordinate import with outputs](09-COORDINATE-IMPORT.md) | Next: [11. Web app behavior](11-WEB-APP.md)
