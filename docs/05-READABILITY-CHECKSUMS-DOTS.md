# 5. Readability, checksums, and dots

[README](../README.md) | Prev: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md) | Next: [6. Hashpaths](06-HASHPATHS.md)

---

Hashsite codes may be copied from bad screenshots, read aloud in emergencies, written by hand, printed on signs, or texted under stress.

Readability matters.

## Character ambiguity

Common problems:

- `O` vs `0`
- `I` vs `1`
- lowercase `l` vs `1`

Hashsite keeps the full 36-symbol alphabet for compactness but mitigates the worst cases:

- canonical letters are uppercase
- input is case-insensitive
- uppercase `O` may be displayed as lowercase `o` to reduce `O/0` ambiguity
- optional dots help chunk and verify strings

## Dots

Example:

```text
7B663IHXB8
7B6.63IH.XB8
```

The dotted and undotted versions refer to the same location.

Dots are placed deterministically from the code content, not arbitrarily.

## Luhn-derived checksum

Hashsite uses Luhn-derived logic as a lightweight transcription check.

The older design explored adding a lowercase checksum character, such as:

```text
#2A0E78^   -> #2A0E78j^
#2AEB71^   -> #2AEB71l^
```

The current dot system keeps the code itself unchanged and places optional dots as readability/checksum helpers.

## Altitude-aware checks

The Luhn-derived dot/check behavior is computed over the full string, including altitude.

That means the same horizontal code with different altitude produces different dot positions.

Use dots when the code will be transcribed by hand, read aloud, printed, or relayed in conditions where a wrong character could matter.

---

[README](../README.md) | Prev: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md) | Next: [6. Hashpaths](06-HASHPATHS.md)
