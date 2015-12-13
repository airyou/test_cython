# -*- coding: utf-8 -*-
__author__ = 'youhei'

import hello as cy
import time

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

s = time.time()
integrate_f(10**7, 10**7, 10**7)
print(time.time() - s)

s = time.time()
cy.integrate_f(10**7, 10**7, 10**7)
print(time.time() - s)

s = time.time()
cy.integrate_f2(10**7, 10**7, 10**7)
print(time.time() - s)

s = time.time()
cy.integrate_f3(10**7, 10**7, 10**7)
print(time.time() - s)

cy.f(2)
cy.f2(2)
#cy.f3(2) #cdefで定義しているのでpython側からは見えない。
