# CLI reference

Build:

```bash
gcc -O2 hashsite.c -lm -o hashsite
./hashsite test
```

## Encode / decode

```bash
hashsite encode 35.222 -101.831 9
hashsite decode 7BA2CSoDZ
hashsite bbox 7B663I
```

## Inspection

```bash
hashsite valid 7B663IHXB8
hashsite precision 9
hashsite precision 9 35.0
hashsite parent 7B663IHXB8
hashsite contains 7B663 7B663IHXB8
```

## Geometry

```bash
hashsite distance 7B663I 76B82D
hashsite bearing 7B663I 76B82D
hashsite midpoint 7B663I 76B82D
hashsite offset 7B663IHXB8 100 50
hashsite neighbors 7B663I
hashsite children 7B663I
```

## Dots and pattern matching

```bash
hashsite luhn 7B663IHXB8
hashsite luhncheck "7B6.63IH.XB8"
hashsite closest 7BA2CSoDZ '$FC64W'
```
