# -*- coding: utf-8 -*-
__author__ = 'youhei'

def say_hello_to(name):
    print("Hello %s!" % name)

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

def f2(double x):
    return x**2-x

def integrate_f2(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f2(a+i*dx)
    return s * dx

cdef double f3(double x) except? -2:
    return x**2-x

def integrate_f3(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f3(a+i*dx)
    return s * dx

cpdef mylist(l, s):
    l.append(s)
    return l
