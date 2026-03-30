![](img/hashsitebanner.png)

# Hashsite

## Public-source Fractal Geocoding Library

by Matt Channon

Hashsite is a compact, human-usable placestamp system for describing where something actually is.

Short codes describe broad areas. Longer codes describe precise handoff points. Add the optional **Z-axis** extension and a Hashsite can describe the correct floor. Add a **hashpath** and it can describe not just a point, but the actual sequence of arrival decisions that gets a person, package, or ambulance to the right place.

**Start here:**

- [Licensing overview](licensing.md)
- [Buy the Hashsite Developer Welcome Kit](/buy/)
- [Full commercial licensing terms](COMMERCIAL-LICENSE.md)
- [Welcome Kit terms](WELCOME-KIT.md)
- [Public-interest fee waiver policy](PUBLIC-INTEREST-WAIVER.md)

---

## 1. Why Hashsite exists

Location still sucks.

Latitudes and longitudes are precise, but awkward for ordinary people to read, repeat, compare, shorten, and authenticate. Street addresses are familiar, but they are often vague, discontinuous, misleading, building-centric rather than door-centric, and terrible at campuses, hospitals, airports, apartment complexes, industrial sites, new construction, rural land, and anywhere the real problem is not *the parcel* but *the path from where you are to where you need to be*.

The biggest failure of existing location systems is not that they cannot describe a point.

It is that real-world arrival often is **not a point problem**.

It is a **path problem**.

Consider:

- a gated apartment complex with several similar mid-rise buildings and poor signage
- a hospital that has expanded three times and now has six viable entrances, two parking structures, and one useless street address
- an airport with multiple pickup levels and duplicate door numbers
- a loading dock or service entrance that is nowhere near the building’s official address
- a tow truck, courier, friend, or paramedic trying to find the *actual* access point at night, in weather, under stress

Traditional street addresses solve this badly. Pure coordinate systems solve only the final point. What3Words and similar systems often solve only a *single lookup target*, and do not naturally express proximity, stepwise movement, or how to get from the curb to the correct door.

Hashsite is designed to solve the whole arrival problem.

### What Hashsite is for

Hashsite is intended for:

- meet here
- put the package here
- park here
- use this gate
- enter here
- go up this staircase
- go to this floor
- deliver to this door
- start here, then follow this route

The ideal output is not “close enough.”

The ideal output is “nobody calls back to say they can’t find it.”

### Hashpath: the real point

A **single point** is often inadequate for real navigation.

A delivery driver does not just need “the property.” They need:

1. where to turn in
2. which gate or driveway to use
3. where to stop or park
4. which entrance matters
5. whether stairs, elevator, loading bay, or lobby is relevant
6. the final handoff point

That is the main pain point in modern wayfinding.

Hashsite addresses this with **hashpath**.

A hashpath is a compact route description built from:

- one or more hashsites
- optional local diffs between them
- optional vertical markers
- optional semantic labels in software or UI

A hashpath turns “go to this point” into “follow this arrival sequence.”

### Why hashpath matters

A static point works well for:

- a picnic table
- a trailhead
- a rural gate
- a broken-down car on a highway shoulder

A static point works badly for:

- apartment complexes
- campuses
- hospitals
- airports
- hotels
- event venues
- warehouses
- multi-entrance office buildings
- pickup and dropoff choreography

Hashpath is the missing layer between raw coordinates and actual arrival.

### A few real-world examples

#### Apartment complex

Instead of only this:

`#9E3ZDC4AX`

you send a hashpath conceptually equivalent to:

- enter complex here
- park here
- use this staircase
- go to this landing
- final door here, 8m above street level

The final door is still a point.

But the success of the trip depends on the path.

#### Hospital

A hospital visit usually has at least four distinct relevant places:

- correct parking structure
- correct exterior entrance
- correct desk or elevator bank
- correct clinic door

A street address gives you none of that.
A point gives you only one of those.
A hashpath can give you all of them.

#### Airport pickup

“Door 08” is useless if there are two Door 08s on different levels.

A hashpath can specify:

- arrivals level curb
- lane or side
- exact standing point
- fallback pickup point if traffic control moves you

#### Delivery

For delivery platforms, the last 30 meters are where the waste happens.

The address got the driver to the parcel.
The app got the driver to the curb.
The customer still gets the text:

> “I’m here.”

Hashpath is meant to eliminate that text.

---

## 2. How Hashsite works

### The basic idea

Hashsite starts from a simple 6x6 grid using capital letters and digits.

![](img/grid2.png)

Fill in the numbers and letters:

![](img/grid3.png)

That is most of the system.

Every Hashsite location may be written with a leading `#`. The `#` is optional, but helpful for recognition in plain text. Vertical information is handled separately in the optional **Z-axis** extension described below.

The point is not novelty for novelty’s sake. The point is to create a location language that is:

- compact
- scalable in precision
- spatially logical
- human-usable
- offline-friendly
- extensible beyond a flat point on a map

### Precision and shortening

Hashsite is designed so that shorter codes describe larger areas and longer codes describe more precise ones.

If one character is good enough, use one character.
If you need the correct doorway or handoff point, use more.

A properly designed location system should not force unnecessary length when the use case is broad, or unnecessary vagueness when the use case is precise.

Any two-character Hashsite, regardless of where it is on Earth, should be approximately 600x600 km, with each additional character reducing the area by another stage of subdivision. Eight characters describe approximately 13x13 m, and nine describe about a 2 meter square.

This means the same notation can be used for:

- regions
- neighborhoods
- buildings
- entrances
- rooms
- doors
- curbside handoff points

### Human logic matters

A major complaint about many alternative addressing systems is that nearby places do not look nearby, and changing one element can teleport you across the globe.

Hashsite is designed around spatial logic rather than obfuscation.

It aims to preserve useful human intuitions such as:

- shorter vs longer means broader vs more precise
- nearby movement should be describable in a structured way
- relative movement should not require a proprietary server
- the notation should still mean something without a network round trip

That matters for:

- trust
- memorability
- debugging
- dispatch
- map reading
- fallback operation
- emergencies

### Pencil-and-paper friendliness

Hashsite is designed so that many directional adjustments can be reasoned about directly.

That does not mean every user will do map math by hand.

It means the system is built on a logic transparent enough that they **could**.

That is a real advantage.

A location system should not become useless the moment a company server disappears, a lookup API is rate-limited, or a user loses connectivity.

### Spheroid optimization

Consider the Mercator projection, including the parts Mercator left off:

![](img/mercator1.png)

Let’s begin by applying our 6x6 grid to it:

![](img/mercator3.png)

This works, but it overrepresents the poles and underrepresents the equator. By adjusting the subdivision, we can make each first-level area equal in size:

![](img/mercator4.png)

The latitude lines are at `0°`, `19.47°`, and `41.81°`, splitting the Earth into six equally sized slices.

Now no matter the first character, we are talking about the same amount of area.

Take `#B`:

![](img/gridb.png)

Split it into a 6x6 grid:

![](img/gridb2.png)

For tropical and mid-latitudes, these are not very square, so we instead use a 9x4 grid:

![](img/gridb3.png)

Accordingly with `#BA`:

![](img/gridc.png)

From the third digit onward, we return to the 6x6 grid:

![](img/gridc2.png)

And `#BA3`:

![](img/gridd.png)

![](img/gridd2.png)

And `#BA3U`:

![](img/gride.png)

The goal is not just elegance. The goal is fairer area representation, shorter useful codes, and more human-coherent subdivision.

### Polar regions

The poles require different handling.

If you took a polar region such as `#1`:

![](img/gridf.png)

and split it into a normal 9x4 or 6x6 grid, you would get absurdly precise longitudes and absurdly imprecise latitudes:

![](img/gridf2.png)

So polar regions are split differently. Instead of `9/9/9/9`, Hashsite uses:

`1/1/2/3/3/4/5/5/6/6`

![](img/gridf3.png)

These do not look square in the projection, but they are much closer in actual represented area.

From there, the system again returns to the ordinary 6x6 grid.

### Checkdots

Hashsite keeps the full 36-value set because the density gain matters.

It also gives decimal points a second job: they act as built-in **checkdots**.

In the base XY code, a Hashsite uses **exactly two decimal points**. Their positions are not chosen by the user and are not tied to whether the nearby characters are digits or letters. Instead, the two checkdots are placed according to a Luhn-style checksum run across the characters in order.

That means:

- letters are always CAPITAL
- exactly two decimal points appear in the base code
- dot placement is checksum-driven, not cosmetic
- the same underlying code always yields the same two dot positions

This helps in two ways at once:

- it breaks up visually ambiguous runs of letters and numbers
- it provides a lightweight typo check when a code is copied, typed, or read aloud

For short codes, the checkdots do little or no work because there are too few places to put them. For longer codes, they become more useful because there are more possible placements and therefore more wrong versions to reject.

#### Concrete example

Suppose the underlying base code characters are:

`#BA3U7K9`

After the checkdot routine runs, the rendered Hashsite might be:

`#BA.3U7.K9`

If someone mistypes or swaps characters and writes:

`#BA.37U.K9`

the checkdots will usually no longer line up with where they are supposed to be for that character sequence. So even before looking the code up on a map, software can notice that the formatting no longer matches the checksum and warn the user that something is probably wrong.

The point is not to make Hashsite impossible to mistype. The point is to catch ordinary human errors early, without making the code longer.

### Z-axis

A real location system should not pretend the world is flat.

The difference between the first floor and the fiftieth floor is not trivia. In an emergency, a delivery, or a meetup, it can be the difference between success and failure.

By default, a Hashsite describes an XY location only.

When you want to add vertical information, you may append an optional `^` and then encode the Z-axis payload after it.

So the core placestamp stays simple:

`#F.6NZ`

And the Z-axis extension begins only when needed:

`#F.6NZ^J` means 1 meter below street level
`#F.6NZ^1` means 1 meter above street level
`#F.6NZ^0` handles the 0m case

This covers most everyday building-navigation situations.

If a second post-caret character is added, it acts like a higher-order digit, multiplying each value by 18.

Examples:

`#F.6NZ^.1.1` = 19 meters above street level
`#F.6NZ^.1.0` = exactly 18 meters above street level
`#F.6NZ^.1I` = exactly 18 meters below street level

A trailing `^` at the end of the Z-axis payload is also optional. When present, it switches the reference frame from street level to sea level.

Examples:

`#F.6NZ^^` = sea level
`#F.6NZ^1^` = 1 meter above sea level
`#F.6NZ^2^J` = 2 meters above a street level that is itself 1 meter below sea level

The system can also extend below 1-meter resolution and above kilometer-scale elevation ranges using additional post-caret characters.

In short: Hashsite is designed to describe the actual place, not a flattened cartoon of it. The base code does not require `^`; the Z-axis extension introduces it only when vertical data matters.

---

## 3. Licensing and project status

### License

Hashsite is **public-source**, not OSI open source.

Hashsite is free for **Free-Tier Users** under the [Hashsite Public License v2.0](LICENSE).

A paid commercial license is required for:

- governments
- militaries
- intelligence agencies
- law-enforcement agencies
- public-sector bodies
- contractors acting on their behalf
- large commercial enterprises

A low-friction **Developer Welcome Kit** is available for users in those paid buckets who need a quick, lawful on-ramp:

- **$999**
- **3-year term**
- **up to 5 named developers**
- **one legal entity**
- **one product, service, or internal program**
- **limited production use**

See:

- [licensing.md](licensing.md)
- [LICENSE](LICENSE)
- [NOTICE](NOTICE)
- [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)
- [WELCOME-KIT.md](WELCOME-KIT.md)
- [PUBLIC-INTEREST-WAIVER.md](PUBLIC-INTEREST-WAIVER.md)
- [Buy the Hashsite Developer Welcome Kit](/buy/)

Licensing contact: **licensing@hashsite.org**

### What a full Hashsite ecosystem looks like

Hashsite is not just a notation. It needs tooling.

The full ecosystem should include:

- reference codecs
- multiple language implementations
- map integrations
- iOS and Android apps
- browser tools
- route builders
- hashpath authoring tools
- delivery and pickup UX
- hospital, campus, airport, and venue templates
- API access where useful
- offline-first client-side logic wherever possible

The ideal user base is not “mapping enthusiasts.”

It is everybody.

### FAQ

#### Do we really need another one of these?

Yes, because the problem is still not solved.

Street addresses solve one part of the problem.
Coordinates solve another.
A practical human placestamp system should solve more of it at once.

#### Can’t existing systems already do this?

Some of the pieces exist elsewhere.

But the combination usually does not:

- compact code
- progressive precision
- logical local movement
- offline friendliness
- vertical support
- route-or-path support
- human legibility
- public implementability

Hashsite is an attempt to put those in one system.

#### Can’t you make the codes smaller?

Only up to a point.

You can always trade completeness or clarity for a shorter token, but that often means giving up oceans, poles, altitude, hand calculation, or human consistency.

Hashsite tries to be short without becoming magical nonsense.

#### Isn’t the real problem just bad signage?

Sometimes, yes.

But bad signage is everywhere, and software should help people survive the world as it is, not the world as a facilities manager imagines it to be.

#### Why not just send a pin?

Pins work until they don’t.

Pins are brittle in screenshots, speech, paper relay, and repeated reuse. They do not themselves express scale, verticality, or arrival sequence.

Hashsite is meant to be a portable placestamp, not merely a UI gesture inside one app.

### Roadmap

1. Finalize the core specification
2. Finalize hashpath notation and delta conventions
3. Publish reference codecs
4. Ship examples in multiple languages
5. Build browser tools
6. Build iOS and Android apps
7. Build delivery, hospital, and campus demos
8. Publish robust documentation and FAQs
9. Evangelize adoption
10. Make arrival less stupid

---

To hear a bunch of HN readers opine on this without seeing it, visit [https://news.ycombinator.com/item?id=19511917](https://news.ycombinator.com/item?id=19511917), do a find for `mchannon`.
