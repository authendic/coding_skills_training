# Prime Factorizations

## introduction

considering the simplest isPrime function:

```python
def isPrime(n):
    ...
    sqrt = int(math.sqrt(n))
    for f in range(2, sqrt+1):
        if n % f == 0
            return False
    return True
```



we can improve the loop, by preventing even num testing  except 2, and test 2 in a separate code

```python
if n < 2:
    return False
if n <= 3:
    return True
if n % 2 == 0:
    return False
for f in range(3, sqrt+1, 2)
    ...
```

this code saving half of the  time in calculating. and we can improve it even more, by preventing nums whose value are multipled by 3 

```python
if n < 2 or n == 4:
    return False
if n <= 5:
    return True
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
if n < 49:
    return True
for f in range(7, sqrt+1, 6): 
    if n % f == 0 or n % (f+4) == 0:
        return False
    ...
```

this code saving nearly 1/3 time of calulating.

## calulating all prime factors 

we can transform the isPrime's loop, to a generator, for factorize a number.  considering the sequence below:

tested prime: 
    - 2, 3, 5, 7 ... Tn
    - Tn is a knowed prime sequence
candidate from loop:
    - C1,Cg1,  C2, Cg2, .... Ck ,Cgk

    Cg(k) = C(k) + 4
    C(k) = Tn + 6 - Tn % 6 + 1 

    if N is not multiple of  2..Tn, C1,Cg1..C(i),Cg(i), and is multiple of C(m), then C(m) must be a prime factor of N.


## references

[sympy/ntheory]: https://github.com/sympy/sympy/blob/master/sympy/ntheory/primetest.py  pip install sympy
[Euler_pseudoprime]: https://en.wikipedia.org/wiki/Euler_pseudoprime
[Miller-Rabin-primality-test]: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants

vim: ft=markdown
