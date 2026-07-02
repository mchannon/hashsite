# Hashpath in Hashsite

Hashsite should treat a received Hashsite as a one-step Hashpath.

A normal map link usually answers: how do I get near the place?

A Hashpath answers: what do I do when ordinary directions stop being enough?

## Editor to reader flow

When a sender pins a red destination and shares it, the recipient should enter reader mode. The sender should be able to preview the exact reader view before sending.

Recommended behavior:

```text
Edit mode:
  Blue third button = 👁 Preview

Reader mode:
  Top-left button = ← Back to editing / Edit this
```

## Blue is local

Blue is the device/browser position. Blue should never be loaded from a shared URL.

## Reader-side enrichment

The reader may compute or display straight-line distances, optional walking/driving estimates, Google Maps directions links, step cards, route-in / route-out buttons, and warnings. These computed facts should not be encoded into the compact Hashpath.
