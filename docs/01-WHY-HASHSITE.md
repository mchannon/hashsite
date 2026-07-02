# 1. Why Hashsite?

[README](../README.md) | Next: [2. Format, codes, and precision](02-FORMAT-CODES-PRECISION.md)

---

Communicating location is hard.

Say you've been in a traffic accident and there are injuries. You're on the phone with emergency services and they want to know where to send the ambulance.

Your phone knows exactly where you are. But you can't share your location over an emergency call once it's connected.

Now imagine it's dark. Or snowing hard. Or you went through trees, down a ravine, into a lake, or all five at once. They need to know where you are to the nearest meter, not the nearest mile.

Launch Hashsite, and now you can read out the letters and numbers that can save your life.

## The current tools

The tools we currently have for communicating location are:

- street addresses
- latitude/longitude strings
- map URLs
- proprietary geocoding products

Each fails in a different way.

## The failure of street addresses

A building address is a billing artifact designed for mail sorting.

It does not tell you:

- which entrance to use
- where to park
- which gate is the service gate
- which of three buildings on a campus is the right one
- where the ambulance entrance is
- where the delivery actually belongs
- where the pickup point is
- which side of a rural property matters

Forget precision and accuracy: addresses often break their own rules.

## The failure of latitude/longitude

Latitude and longitude are globally consistent and machine-readable.

They are also verbose, non-hierarchical, easy to transpose, impossible to shorten meaningfully, and flat.

Swapping two digits produces a different but plausible-looking location with no indication of error.

Their precision is deceptive. Most people have no intuition for what a difference of `0.001°` means on the ground, so coordinates imply false exactness while being difficult to sanity-check by eye.

Reading `35.2220, -101.8310` aloud over a phone in a noisy environment or while injured is a meaningful failure mode.

## The failure of map URLs

Map URLs work, but they are long, opaque, app-specific, and full of noise:

- tracking parameters
- app state
- routing assumptions
- search-result context
- map-provider dependencies
- unreadable query strings

They are useful to machines and apps, but poor human objects.

## What3Words sucks — and why that matters

One company has raised over £150 million on the premise of assigning three random English words to every 3-meter cell on Earth and marketing it to emergency services.

It has also:

- sent ambulances to the wrong location dozens of documented times due to structurally unavoidable confusable word pairs
- threatened researchers who published analysis of the system
- issued DMCA takedowns against open-source implementations
- encrypted its wordlist inside a mobile app to prevent interoperability
- persuaded emergency services to depend on a system whose offline function requires payment and whose terms can change

That is not infrastructure. That is a hostage.

There is a long tradition of empires charging people for what they could make themselves: taxing salt, outlawing spinning wheels, requiring permits to collect rainwater. What3Words is that tradition applied to location data: a thing that costs nothing to produce, artificially enclosed, then rented back at a price set by the encloser.

## What Hashsite does instead

**Offline-first.** The full codec can run locally. No network, API key, server, or permission.

**Hierarchical.** `#7B663I` is contained within `#7B663`; `#7B663` is contained within `#7B6`.

**Compact.** Nine characters gives person-scale precision and fits in text messages, QR codes, verbal exchange, sticky notes, printed instructions, and forms.

**3D-native.** Altitude is part of the format, not an afterthought.

**Path-aware.** A real arrival problem is often a path problem, not merely a point problem.

**Not word-based.** The confusable-pair problem does not exist in the same way because Hashsite does not rely on words.

---

[README](../README.md) | Next: [2. Format, codes, and precision](02-FORMAT-CODES-PRECISION.md)
