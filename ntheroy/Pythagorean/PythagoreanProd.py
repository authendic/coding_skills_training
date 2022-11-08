#!/usr/bin/env python3
# *-* encoding:utf8 *-*
#  vim: colorcolumn=80

# >> 1

def is_Pythagorean(n):
    for c in range(n//3+1, n):
        b_a_square = c * c + 2 * n * c - n * n
        if b_a_square<1:
            continue
        b_a = int(b_a_square ** 0.5)
        if b_a * b_a != b_a_square:
            continue
        b = (n - c + b_a) //2
        a = n - c - b
        if 0 < a < b < c:
            return a, b, c, n
    return False

print(is_Pythagorean(12))
print(is_Pythagorean(2001))
print(is_Pythagorean(3000))
# >> 1
