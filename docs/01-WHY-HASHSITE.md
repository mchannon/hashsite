# 1. Why Hashsite?

[README](../README.md) | Next: [2. Format, codes, and precision rubric](02-FORMAT-CODES-PRECISION.md)

---

Communicating location is hard.

Say you've been in a traffic accident and there are injuries. You're on the phone with emergency services and they want to know where to send the ambulance.

Your phone knows exactly where you are. But you can't share your location over an emergency call once it's been connected.

Now imagine it's dark. Or snowing hard. Or you went through trees, down a ravine, into a lake, or all five at once. They need to know where you are to the nearest meter, not the nearest mile.

Launch Hashsite, and now you can read out the letters and numbers that will save your life.

## The failure of street addresses

A building address is a billing artifact designed for mail sorting.

It does not tell you:

- which entrance to use
- where to park
- which gate is the service gate
- which of three buildings on a campus is the right one
- where the ambulance entrance is
- where the delivery actually belongs

Addresses are not precise enough for many real arrival problems.

## The failure of lat/lon

Latitude and longitude are globally consistent and machine-readable.

They are also verbose, non-hierarchical, easy to transpose, impossible to shorten meaningfully, and flat.

Swapping two digits produces a different but plausible-looking location with no indication of error. Most people have no intuition for what a difference of `0.001°` means on the ground.

Reading `35.2220, -101.8310` aloud over a phone in a noisy environment or while injured is a meaningful failure mode.

## What Hashsite does instead

Hashsite gives locations a compact, hierarchical, human-shareable, offline-capable code.

```text
#7BA2CSoDZ
```

Hashsite does not make lat/lon disappear. It wraps geographic coordinates in a more usable human and software object.

---

[README](../README.md) | Next: [2. Format, codes, and precision rubric](02-FORMAT-CODES-PRECISION.md)
