#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
import fontforge

curfnt = fontforge.open(argv[1]+".sfdir")

# First pass : remove overlap, fix direction, add extrema
curfnt.selection.all()
curfnt.removeOverlap()
curfnt.correctDirection()
curfnt.addExtrema()

# replace references by copies ?

# prepare flags
genflags = ("opentype", "dummy-dsig")
# export otf, woff
curfnt.generate( argv[1]+".woff", flags=genflags)
curfnt.generate( argv[1]+".otf", flags=genflags)

# ttf export preparation : make all curves quadratic
for layer in curfnt.layers:
    curfnt.layers[layer].is_quadratic = True
# export otf
curfnt.generate( argv[1]+".ttf", flags=genflags)

# rewind
curfnt.revert()
