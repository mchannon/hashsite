# 13. Word mode and legacy ideas

[README](../README.md) | Prev: [12. Design and build philosophy](12-DESIGN-BUILD-PHILOSOPHY.md) | Next: [14. Roadmap, W3WNKER, license, and companions](14-ROADMAP-W3WNKER-LICENSE-COMPANIONS.md)

---

The earliest Hashsite notes explored additional human interfaces beyond the raw alphadecimal code.

These are not the current center of the implementation, but they explain design space and are worth preserving.

## Word mode

Unlike What3Words’ patented scheme for deriving three disjointed words from a location, the Hashsite approach was not to take spatial coordinates, squash them into one huge integer, and then map that through an opaque randomized wordlist.

The old concept was to take 2-character alphadecimal “bytes” and run them through open-source alphabetic dictionaries in a deterministic order to construct a sentence.

The proposed parts of speech were:

1. Nouns
2. Adjectives
3. Possessives
4. Verbs
5. Predicate objects or predicate adjectives

So a detailed Hashsite like:

```text
#M2DE3200ZZ^
```

could be read through a dictionary pattern like:

```text
33 22 11 44 55
```

and become something like:

```text
John's green raincoat is dirty
```

The purpose was not to imitate What3Words. The point was to show that human-memorable location phrases can be generated openly and deterministically if desired.

## Vertical word extension

The older word-mode notes also imagined vertical components following the caret as a proper name at the end of the sentence.

Example concept:

```text
#M2DE3200ZZ^2I
```

could become:

```text
John's green raincoat is dirty, Michelle.
```

Again, this is legacy design exploration, not the main current codec surface.

## Error-correction character idea

The early notes explored adding a lowercase checksum character before the terminator:

```text
#2A0E78^  -> #2A0E78j^
#2AEB71^  -> #2AEB71l^
```

That idea preserved code compactness but risked visual confusion in some fonts. The current dot/check approach is cleaner for the present implementation.

## Why preserve this page?

Because Hashsite is not only a codec. It is an argument about open, human-usable location infrastructure.

The word-mode and checksum-character ideas show alternate surfaces for the same underlying principle:

```text
open spatial truth should not be trapped inside a proprietary black box
```

---

[README](../README.md) | Prev: [12. Design and build philosophy](12-DESIGN-BUILD-PHILOSOPHY.md) | Next: [14. Roadmap, W3WNKER, license, and companions](14-ROADMAP-W3WNKER-LICENSE-COMPANIONS.md)
