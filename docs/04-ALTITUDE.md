# Altitude / 3D locations

Hashsite is 3D-native.

Altitude is encoded after `^`.

Examples:

```text
#7BA2CSoDZ^1
#7BA2CSoDZ^S
#7BA2CSoDZ^I1I
```

## Coarse mode

The first character after `^` is signed base-36.

| Character | Meaning |
|---|---|
| `0` | 0 m |
| `1`–`H` | +1 to +17 m |
| `J`–`Z` | −1 to −17 m |
| `I` | switch to precision mode |

## Precision mode

Precision mode begins with `^I`.

Examples:

```text
^I1I = +1.5 m
^IJI = -1.5 m
```
