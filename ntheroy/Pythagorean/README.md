# Pythagorean

A Pythagorean triplet is a set of three natural numbers, `a < b < c` and satisfied : `a^2 + b^2 = c^2`

Given `N` , Check if there exists any Pythagorean triplet for which `a + b + c = N`
Find maximum possible value of `a·b·c`  among all such Pythagorean triplets, If there is no such Pythagorean triplet print `-1`.

## resolve

```
a^2 + b^2 = c^2   ①
a + b + c = N     ②

from ②
    => (a+b)^2 = (N-c)^2
    => a^2 + 2ab + b^2 = N^2 -2Nc + c^2
replace using ①
    => c^2 + 2ab = N^2 - 2Nc + c^2
    => 2ab = N^2 - 2Nc    ③

②  -  ③
    => a^2 + b^2 - 2ab = c^2 - N^2 + 2Nc
    => (a - b) = N^2 - 2Nc + c^2
because a < b:
    b - a = (N^2 - 2Nc + c^2)^0.5    Ⅰ
    a < b < c =>  c > N//3           Ⅱ
```

acording formular Ⅱ, we can try every c > N//3. If `c` satisfied formular Ⅰ, `b-a` is an integer larger than 1.





## 参考

