![](hashsitebanner.png)

Open-source Geocoding Library

Paradigm/How-to

Geocoding is all about representing a fixed point in space in as short and reproducible a way as possible. If it can be done simply, so much the better.

Hashsite’s primary philosophy is 5.5-bit alphadecimal encoding. It sounds complicated but it’s actually quite simple.

Start with a 6x6 grid:

Fill in the numbers and letters (capital letters only):

And this is mostly it.

Every hashsite location has a prefix of “#$”.  The prefix is optional, but lends itself well toward identifying what is intended.

So let’s start with applying our 6x6 grid to our old friend the Mercator projection:

This works, but it overrepresents the area at the poles and underrepresents the area at the equator.  By using the 6x6 grid, we can tweak this a bit to make each area equal:

The lines are at 0°, 19.47°, and 41.81°.
Now no matter the first character, we’re talking about the same amount of area.

So let’s take #$F and split it into a 6x6 grid:

These aren’t very square, so for tropical and mid latitudes, we use a 9x4 grid, 9/9/9/9:

For the third digit on, we go back to the 6x6 grid:

accordingly with #$F6:

And #$F6N:

And #$F6NZ:

There. Compare #$F6NZ with these other encoding systems:

There’s one more thing to remember with Hashsite: the polar regions.

If we split a polar region (say, #$2) into a 9x4 or even a 6x6 grid, we’d find ourselves with ridiculously accurate longitudes and ridiculously inaccurate latitudes:

So for polar regions only, we split it differently; instead of 9/9/9/9, we use 1/1/2/3/3/4/5/5/6/6:

And from there, we also go back to the 6x6 grid:

Any two-character hashsite, regardless of where it is on Earth, should be approx. 600x600 km, with each additional character taking off a power of 6x6, so 100x100km, ~16x16km, and so on. Eight characters will describe approx. 13x13m, and nine will describe a 2 meter square.

There’s nothing wrong with shortening your hashsite code, as each hashsite is presumed to be the center of the grid square. If one character is good enough to represent your site, you can use one character.

That’s all you need to know about Hashsite, but here are some more features:

*Decimals

It’s well-known that o and 0 look a lot alike, and I, l, and 1 look a lot alike.  Most geocoding systems take steps to avoid this problem.  But in order for Hashsite to have 36 values, we have to use every letter and number.  

All Hashsite letters are CAPITAL. It’s not yelling, it’s practical.

This means no problems with lowercase L: getting a 1 and a capital L confused is not likely. Getting a capital O and a numeric 0 with a slash should be also unlikely. Nonetheless, we can add dots into a hashsite to help avoid the difference. Dots can and should go before any number (0 and 1 in particular) but never before any letter. They are not required, but they help people understand the difference between:

#$L.1L.0OL (20 miles NE of Moscow):

and #$LLLO.0.1 (30 miles NW of Abu Dhabi):

So if you’re going to tweet where the party at the old quarry is going to be, you can leave the dots in there and ignore them when punching them into your Hashsite-enabled map app.

*Vertical space

To add a message regarding vertical space, we add a carat to the end:

#$F.6NZ^

Then we use the same 6x6 grid in the following manner:

So #$F.6NZ^I would mean 1 meter below street level, and #$F.6NZ^H would mean 1 meter above street level. This covers -18m to 18m inclusively (#$F.6NZ^, the carat followed by no character, handles the 0m case). This covers most everyday wayfinding situations involving up to 6-story buildings.

As soon as you precede the initial post-carat character with a second character, it acts as a sort of conventional “tens digit”, multiplying each value by 18:

#$F.6NZ^.1H would thus be 19 (1 x 18 + 1) meters above street level.  How would we do 18 meters above street level? #$F.6NZ^00, the first zero being a special case indicating we’re at exactly 18. #$F.6NZ^0Z would equal exactly 18 meters beneath street level.

Finally, trailing the entire hashsite with a second carat means that the vertical number is relative to sea level, not street level. #$F.6NZ^^ means we’re at sea level, #$F.6NZ^H^ means 1 meter above sea level.

*Word mode

Unlike What3Words’ patented scheme for deriving three words from a location, the hashsite approach isn’t to take spatial coordinates and squish them into a huge single number which we bust apart again. We simply take the 2-character alphadecimal “bytes” (1332 unique values, 1296 for each possible pair and another 36 for single characters) and run them through an open-source alphabetic dictionary, in alphabetical order.

#$DF28 might end up being #$eager-badger.  #$DF28ML might be #$eager-badger-possum. All the words are 2-7 letters long, common, without spaces or punctuation, alphabetical, and we don’t use plurals to confuse people.  Best off, if you get #$eager-badger and #$eager-badge confused, you’re still close enough to have a shot at figuring things out.
