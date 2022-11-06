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

def prime_candidates(to_include):
    yield 2
    yield 3
    beg = 5
    if to_include % 6 == 0:
        to_include -= 1
    end = to_include - to_include % 6 - 1
    while beg <= end:
        yield beg
        yield beg + 2
        beg += 6
    if beg == to_include:
        yield beg


def prime_factors_v2(n):
    if n < 2:
        return []
    factors = [0]
    f_counts = [0]
    for p in prime_candidates(n**0.5):
        while n % p == 0:
            if p != factors[-1]:
                factors.append(p)
                f_counts.append(1)
            else:
                f_counts[-1] += 1
            n = n // p
            if n == 1:
                break
    if n != 1:
        factors.append(n)
        f_counts.append(1)
    return factors[1:], f_counts[1:]


def prime_factors_v1(n):
    if n == 0:
        return []
    if n < 3:
        return [n]
    factors = []
    if n < 150:
        end = n // 2
    else:
        end = int(n ** 0.5)
    for p in prime_candidates(end):
        while n % p == 0:
            factors.append(p)
            n = n // p
        if n == 1:
            break
    if n != 1:
        factors.append(n)
    return factors


def choice_combine(*pows):
    if len(pows) == 1:
        for n in range(pows[0]+1):
            yield [n]
    if len(pows) > 1:
        for n in range(pows[0]+1):
            for pl in choice_combine(*pows[1:]):
                yield [n] + pl
    return []


def all_factors(n):
    facts, fcnts = prime_factors_v2(n)
    factors = []
    for c in choice_combine(*fcnts):
        v = 1
        for i in range(len(c)):
            v *= facts[i] ** c[i]
        factors.append(v)
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
    for p in prime_candidates(end):
        if n % p == 0:
            return n == p
    return True


# >> 1

if __name__ == "__main__":
    print(prime_factors_v2(20))
    print(prime_factors_v2(228))
    print(prime_factors_v2(1599998640000299))
    print(prime_factors_v2(1599998640000289))
    print(prime_factors_v2(10000330202725801))
    print(isprime(1599998640000289))  # false
    print(isprime(39999983))
    print(isprime(100001651))
    print(all_factors(1599998640000289))
    print(sorted(all_factors(1599998640000299)))

# >> end
