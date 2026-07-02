# 12. Design and build philosophy

[README](../README.md) | Prev: [11. Web app behavior](11-WEB-APP.md) | Next: [13. Word mode and legacy ideas](13-WORD-MODE-AND-LEGACY-IDEAS.md)

---

## Design principles

### Fractal by default

Hashsite is meant to be shortened and extended naturally.

### Offline matters

The format should be encodable and decodable without permission from anybody.

### Human readability still matters

That is why dotted forms, optional markers, and a consistent character set exist.

### 3D should not be bolted on later

Altitude belongs in the format family.

### Interoperability is practical

Hashsite can import other coordinate formats instead of pretending they do not exist.

### The map is an interface

The short code is the durable object.

## Build philosophy

Hashsite is written in plain C with a small, readable public API.

The project aims for:

- low dependency count
- auditability
- embeddability
- portability
- library-first design
- CLI visibility for testing and demos

This makes it suitable for:

- servers
- command-line utilities
- embedded systems
- mobile wrappers
- mapping tools
- disaster-response workflows
- offline field software

---

[README](../README.md) | Prev: [11. Web app behavior](11-WEB-APP.md) | Next: [13. Word mode and legacy ideas](13-WORD-MODE-AND-LEGACY-IDEAS.md)
