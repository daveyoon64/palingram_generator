# Palingram Generator

## What's a Palingram?
A palingram is a series of words that uses the same letters forwards and backwards.

For example:
A man a plan a canal panama

## What does this project do?
This is a small program that a plain dictionary and finds all the 2 word combinations. 

Some example:
yobi boy
tuno nut
trope report

## What? How does this work?

### For two words
1. Compare a word against its reversed version.
2. From the beginning of the word and the end of the reversed word, compare until equal.
3. Repeat step 2, but in reverse (end of word vs. the beginning of the reversed word)

## Technologies use
Python 3.7+
virtualenv

## Changelog
10/13/2019
- Got the general algorithm working
- This version uses the spellcheck library from /usr/share/dict/words
- I want to make a nicer interface for this. Since it generates 11,304 palingrams for a list of ~200,000 words.