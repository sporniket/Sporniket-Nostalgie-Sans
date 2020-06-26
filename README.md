# Sporniket Nostalgie v2

*Sporniket Nostalgie v2* is a collection of fonts inspired by the Atari ST system : its system fonts ('high resolution' 8×16, 'low resolution' 8×8, 'tiny' 6×6), mouse pointers (standard, bee, ...) and default icons (drive icons, file and folders icons).

## v2 Roadmap

The collection will provide the following fonts, mostly in this order of making :
* _DOING_ - a 'console' variant
* _PLANNED_ - a 'console small' variant
* _PLANNED_ - a 'console tiny' variant
* _MAYBE_ - a 'sans-serif' variant
* _MAYBE_ - a 'serif' variant
* _MAYBE_ - an 'icon' variant

## Sporniket Nostalgie v2 — console variants

A set of fixed width fonts inspired by the 8×16 ('console'), 8×8 ('console small') and 6×6 ('console tiny') system fonts. The motto of these fonts : «faithful on screen, beautiful on paper».

### Roadmap 2020

*Summer*

* v2.0.0-alpha : 'console' ; US-ASCII a.k.a Basic latin (any printable character from code 32 —space— to 127).
* v2.0.0-beta : 'console' ; usual diacritic for French : acute, grave and circonflex accents, c with cedilla, 'oe' and 'ae' ligatures.
* v2.0.0 : 'console' ; Latin-1 Supplement.

*Fall*

* v2.1.0-alpha : 'console small' ; US-ASCII a.k.a Basic latin (printable character from code 32 —space— to 127).
* v2.1.0-beta : 'console small' ; usual diacritic for French : acute, grave and circonflex accents, c with cedilla, 'oe' and 'ae' ligatures.
* v2.1.0 : 'console small' ; Latin-1 Supplement.

*Winter*

* v2.2.0-alpha : 'console tiny' ; US-ASCII a.k.a Basic latin (printable character from code 32 —space— to 127).
* v2.2.0-beta : 'console tiny' ; usual diacritic for French : acute, grave and circonflex accents, c with cedilla, 'oe' and 'ae' ligatures.
* v2.2.0 : 'console tiny' ; Latin-1 Supplement.

### Additionnal wish list

If I feel motivated enough, here are some 'nice to have' features that I would like to implement :

* coding special ligatures for console variants : C/Java operators, Pascal ':=' ; however, I would not implement ligatures that are incompatible with GFA-Basic, like '!=' (e.g. setting the value of the boolean variable `a!` to `TRUE` will result in the sequence `a!=TRUE` ; a ligature for C/Java `!=` -not equal- would render the the font unsuitable to write GFA-Basic programs).

* the 'bee'/'honeybee' emoji.

* the standard mouse cursor

* the arrows

## Licence

This project is licenced under the [SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007](http://scripts.sil.org/OFL)

---

# Sporniket Nostalgie Sans v1

> This version is deprecated and will be superseded by version 2.0.0. It will be removed when releasing version 2.1.0, and will be accessible only through a specific tags in this repository.

*Sporniket Nostalgie Sans* is an opentype font project that is inspired by the Atari ST system 8×16 font.

The goal is that at a certain size, the rasterization of the glyphes will look like the aformentioned font. However,
it will not always be perfect, so that it looks more coherent or nice to my taste.

Especially :
* The ampersand `&` glyph is a condensed `Et`.
* As the name imply, the font is a 'sans serif' font, so any serif has been removed, and so uppercase `I` is a simple
vertical stick.
* The vertical metrics has been choosen so that glyph with diacritic like `É` are not deformed like on the original font.
