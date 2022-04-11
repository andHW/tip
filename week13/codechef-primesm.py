# https://www.codechef.com/APRIL221C/problems/PRIMESM

"""
Prime numbers
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

15 5+5+5
20 5+5+5+5

gcd >1 : diff = 0

Intuition:
2 and 3 can create all numbers starting from 2... => maxdiff = 1
2
3
4  <= 2+2 # special: can only be created by 2s
5  <= 3+2
6  <= 3+3 || 2+2+2
7  <= 3+2+2
8  <= 3+3+2
9  <= 3+3+3 || 3+2+2+2
10 <= 3+3+3+2

P,Q >= 2
***THIS IS IMPORTANT FOR PRINTING -1***

## Testcases
2
3 6 -> 0
{3}, {3,3}
3 2 -> 1
{3} {2} -> 1
"""

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def ans(a, b):
    ab = [a, b]
    if min(ab) < 2:
        return -1
    if math.gcd(a, b) > 1:
        return 0
    return 1


ttt = int(input())
for _ in range(ttt):
    a, b = map(int, input().split())

    print(ans(a, b))
