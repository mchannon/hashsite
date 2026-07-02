# 11. Web app behavior

[README](../README.md) | Prev: [10. Pattern matching and suffixes](10-PATTERN-MATCHING.md) | Next: [12. Design and build philosophy](12-DESIGN-BUILD-PHILOSOPHY.md)

---

The Hashsite web app is the public map/share surface.

It should support:

- current location
- map point selection
- code display
- copy actions
- SMS/text actions
- Google Maps links
- reader mode
- preview mode

## Blue, green, red

Blue is the current local/device position.

Green is a selected/reference point.

Red is the target/destination/share point.

## Blue is local

Blue should never be loaded from a shared URL.

A received link can define the shared point, but it should not pretend to know the recipient's current position.

## Reader mode

Opening a shared Hashsite should feel like opening a location card, not accidentally entering an editor.

## Preview mode

The sender should be able to see what the recipient will see before sending a link.

## Current web app identity

The app title bar should reinforce the core product:

```text
#hashsite
open geocoding · no api key · no rent
```

The app is the map interface. The code is the durable object.

---

[README](../README.md) | Prev: [10. Pattern matching and suffixes](10-PATTERN-MATCHING.md) | Next: [12. Design and build philosophy](12-DESIGN-BUILD-PHILOSOPHY.md)
