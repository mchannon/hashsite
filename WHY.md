![Hashsite banner](img/hashsitebanner.png)

# Why Hashsite?

Location is still broken.

Not for machines — GPS coordinates work fine for machines. For people. For the actual human moment of saying "meet me here" or "deliver to this door" or "the ambulance needs to go to this entrance, not that one."

The tools we have for that moment are: street addresses, lat/lon strings, and a small collection of proprietary geocoding products that have done their best to lock that problem up behind a paywall and a terms of service.

None of them solve it well. Here is why, and here is what Hashsite does instead.

---

## The failure of street addresses

A street address tells you which parcel the post office has on file. It does not tell you:

- which entrance to use
- where to park
- which gate is the service gate
- which of the three buildings on the campus is the right one
- what floor the loading dock is on
- where the ambulance entrance is versus the main entrance
- how to get from the curb to the correct door

This is not a niche problem. It is the dominant problem in last-mile logistics, emergency dispatch, hospital navigation, airport pickup, and anywhere the built environment is more complex than a single front door facing a numbered street.

A building address is a billing artifact. It was designed for mail sorting, not for arrival. Using it as a navigation endpoint is borrowing a tool from a different job.

---

## The failure of lat/lon

Latitude and longitude are precise, unambiguous, and globally consistent. They are also:

- **verbose** — a full coordinate pair is 20+ characters that contain no spatial logic a human can use
- **not hierarchical** — you cannot shorten `35.2220, -101.8310` to get a coarser location; you just get a wrong location
- **hard to relay** — reading `35.2220, -101.8310` aloud over the phone in a noisy environment or while injured is a meaningful failure mode
- **easy to transpose** — swapping two digits in a coordinate produces a different but plausible-looking location with no indication of error
- **flat** — coordinates describe a point on a surface; the real world has floors

Coordinates work well as a machine-room foundation. They work poorly as a communication layer between people.

---

## The failure of word-based geocoding

One company has built a system that assigns three random English words to every 3-meter cell on Earth and marketed it aggressively to emergency services.

It has raised over £150 million.

It has also:

- sent ambulances to the wrong location dozens of documented times due to algorithm-induced confusable word pairs
- threatened researchers who published peer-reviewed analysis of its safety failures
- issued DMCA takedowns against open-source implementations
- convinced 85% of UK emergency services to depend on a proprietary system whose offline functionality requires payment and whose word list is encrypted inside a mobile app

The confusable word pairs are not a bug that slipped through. They are a structural consequence of using a linear congruence generator to shuffle 57 trillion cells into a 40,000-word vocabulary. Researchers published this analysis in PLOS ONE in 2023. The company's response was legal threats.

The underlying algorithm is documented in their patent. The wordlist is encrypted. You are permitted to use their API, on their terms, for as long as they choose to offer it, at whatever price they set.

That is not infrastructure. That is a hostage.

---

## What Hashsite does instead

### It works offline

The full encoder and decoder are a single C file. No network. No API key. No server. No permission. Compile it and it works on anything with a C compiler — servers, phones, embedded systems, field laptops without connectivity, disaster response gear.

### It is hierarchical

`#7B663` contains `#7B663I`. `#7B663I` contains `#7B663IHXB8`. You can shorten a Hashsite to zoom out or extend it to zoom in. Parent, child, and neighbor relationships are all computable without any external data or lookup table.

This means you can build spatial indexes, search windows, adjacency logic, and region queries from the codes themselves, without a geometry library.

### It is compact

| Characters | Precision |
|---|---:|
| 6 | ~859 m (neighborhood) |
| 7 | ~143 m (city block) |
| 8 | ~24 m (building entrance) |
| 9 | ~4 m (person-scale) |
| 10 | ~0.7 m (sub-meter) |

Nine characters at sub-4-meter precision fits in a text message, a QR code, a verbal exchange over radio, or a sticky note on a mailbox. The full character set is 0–9 and A–Z, with lowercase `o` substituted for uppercase `O` to eliminate the most common visual ambiguity. No ambiguous characters. No words that sound like other words.

### It is 3D native

Altitude is part of the format, not an afterthought. A single additional character after `^` encodes altitude in signed base-36, covering ±17m per character up to ±838km at four characters, with a precision mode for sub-meter vertical resolution. The correct floor of a hospital or parking structure is not optional information in an arrival workflow.

### It describes arrival, not just a point

A Hashpath is multiple Hashsites concatenated:

```
#7BA2CKG^A#7BA2CSo#7BA2CSoDZ^J
```

This is not a list of coordinates. It is an arrival sequence — gate, parking, staircase, door. The problem of getting someone from where they are to where they need to be is a path problem, not a point problem. Hashsite addresses this natively.

### The confusable pair problem does not exist here

Hashsite does not use words. It does not use a shuffle algorithm with documented near-periodicity that produces confusable siblings. The only ambiguity mitigation needed is `O` → `o`, which is a typographic choice, not an algorithm.

If you read `#7B6.63IH.XB8` and transcribe it wrong, the Luhn-derived dots catch common errors. If you get one character wrong, you land in a nearby cell, not across town.

---

## Who Hashsite is for

**Developers** who are tired of building on top of someone else's API terms.

**Emergency services** who need a location system that cannot be taken down, cannot change its pricing, and does not send responders to the wrong location because two words sound alike.

**Logistics and delivery** platforms where the last 30 meters are where the failures happen and a street address is not a useful endpoint.

**Field teams** — search and rescue, disaster response, survey crews — who work without reliable connectivity and cannot afford API failures.

**Anyone** who thinks location is basic infrastructure and basic infrastructure should not require a subscription.

---

## Why now

The patent landscape around proprietary geocoding has created a chilling effect. Open implementations have been DMCA'd into oblivion. Researchers have been threatened. Emergency services have been locked in.

The correct response to that situation is not to wait for the patents to expire.

It is to build something better, make it free, and let the market work.

Hashsite is that. It is not trying to win a marketing war with a company that has raised £150 million. It is trying to make that marketing war irrelevant.

---

## The bottom line

**What3Words** sends ambulances to the wrong location and sues researchers who say so.

**Lat/lon** is precise and unreadable.

**Street addresses** are billing artifacts.

**Hashsite** is compact, hierarchical, 3D-native, offline-capable, path-aware, open, and free.

Use it because it is better. Distribute it because it cannot be taken away.

---

→ **[Tech Specs](TECHSPECS.md)** — format details, CLI reference, library API

→ **[License](LICENSE.md)** — what you can do and what requires a commercial license
