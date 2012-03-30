#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
# This is an example implementation of pytron

from pytron import pytron

py = pytron()
print "Printing 1st quote:"
print py.get_quote(1)
print "Printing random quote"
print py.random_quote()