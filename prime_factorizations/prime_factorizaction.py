#!/usr/bin/env python3
# *-* encoding:utf8 *-*
#  vim: colorcolumn=80

###############################################################################
# filename  : prime_factorizaction.py
# created   : 202-11-06
# author    : daniel
# description:
###############################################################################

# >> 1
import math


def prime_candidates(from_include, to_include):
    # prime_candidates designed for large then 7,
    # so if from_include less then 7,
    # the function will allways yield 2 3 5.
    if from_include < 7:
        yield 2
        yield 3
        yield 5
        from_include = 7

    if from_include % 6 <= 1:
        beg = from_include - from_include % 6 + 1
    else:
        beg = from_include - from_include % 6 + 5
        if beg < to_include:
            yield beg
        else:
            return
        beg += 2
    lastend = 0
    if to_include % 6 == 0:
        end = to_include - 1
    elif to_include % 6 <= 4:
        lastend = to_include - to_include % 6 + 1
        end = lastend - 2
    else:
        end = to_include
    while beg <= end:
        yield beg
        yield beg + 4
        beg += 6
    if lastend:
        yield lastend


def prime_factors(n):
    if n == 0:
        return []
    if n < 3:
        return [n]
    factors = []
    if n < 150:
        end = n // 2
    else:
        end = int(n ** 0.5)
    for p in prime_candidates(2, end):
        while n % p == 0:
            factors.append(p)
            n = n // p
        if n == 1:
            break
    if n != 1:
        factors.append(n)
    return factors

def isprime(n):
    if n < 2:
        return False
    if n < 6:
        return n != 4
    if n < 150:
        end = n // 2
    else:
        end = int(n ** 0.5)
    for p in prime_candidates(2, end):
        if n % p == 0:
            return n == p
    return True

# >> 1

if __name__ == "__main__":
    print(prime_factors(20))
    print(prime_factors(228))
    print(prime_factors(1599998640000299))
    print(prime_factors(1599998640000289))
    print(prime_factors(10000330202725801))
    print(isprime(1599998640000289))
    print(isprime(39999983))
    print(isprime(100001651))
    for c in prime_candidates(10000330202725801, 10000330202725801+100):
        if isprime(c):
            print(c)

#     import sympy
#     %timeit -n 10 sympy.isprime(10000330202725901)
#     %timeit -n 3 isprime(10000330202725901)
#     %timeit -n 10 pow(2, 10000330202725901, 10000330202725901)

# >> end
