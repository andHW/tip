# https://codeforces.com/contest/1658/problem/B
import sys
from itertools import permutations
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

"""
# My pattern finder
for n in range (1, 50):
    print(f"n={n}")
    perms = permutations(range(1,n+1), n)
    ans = 0
    for p in perms:
        magic = [(i+1)*v for i,v in enumerate(p)]
        gcd = math.gcd(*magic)
        if gcd>1:
            print(p)
            print(magic)
            print(f"gcd:{gcd}")
            ans+=1
    print(f"n={n} | ans = {ans}")
"""

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    if n%2 == 0:
        ans = math.factorial(n//2)**2
        print(ans%998244353)
    else:
        print(0)
