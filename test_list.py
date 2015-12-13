# -*- coding: utf-8 -*-
__author__ = 'youhei'

import hello as cy
import time


def mylist(l, s):
    l.append(s)
    return l

s = time.time()
l = []
for i in xrange(0, 10**7):
    l = mylist(l, i)
print(time.time() - s)

s = time.time()
l = []
for i in xrange(0, 10**7):
    l = cy.mylist(l, i)
print(time.time() - s)
