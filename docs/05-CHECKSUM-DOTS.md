# 5. Checksum dots and readability

[README](../README.md) | Prev: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md) | Next: [6. Hashpaths](06-HASHPATHS.md)

---

Hashsite supports optional checksum dots.

Example:

```text
#7B6.63IH.XB8
```

The dots are placed deterministically from the string content, not arbitrarily.

A dotted Hashsite describes the same location as the undotted one.

## Why dots matter

Hashsites may be:

- read aloud
- written by hand
- printed on signs
- texted under bad conditions
- copied from screenshots
- used during emergencies

Dots help chunk the code visually and catch transcription errors before they matter.

## Altitude-aware checksum

The Luhn checksum is computed over the full string, including altitude.

That means the same horizontal code with different altitude produces different dot positions.

Use dots when the code will be transcribed by hand, read aloud, or relayed in conditions where a wrong character could matter.

---

[README](../README.md) | Prev: [4. Altitude and 3D](04-ALTITUDE-AND-3D.md) | Next: [6. Hashpaths](06-HASHPATHS.md)
