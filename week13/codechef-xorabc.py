# https://www.codechef.com/APRIL221C/problems/XORABC

"""
A XOR B + B XOR C + C XOR A
There must be a better solution...
Mine is simply bruteforcing the patterns and somehow my "model" works.
I don't have any proof that it's correct.
(I can proof it by brute forcing, but it means nothing and takes so long...)
"""

from collections import defaultdict
from email.policy import default
import sys
import math
import itertools

debug = False
debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def x(a,b,c):
    return (a^b)+(b^c)+(c^a)

# pattern finder
""" combD = defaultdict(list)
for i in itertools.combinations(range(0,2**8),3):
    combD[x(*i)].append(i)

for i in sorted(combD.keys()):
    found = False
    for t in combD[i]:
        if t[-1] == i//2:
            dprint(f"{i} {bin(i)} {t}")
            found = True
            break
    if not found:
        dprint(f"{i}: NOOOOOOOOOOOO")
dprint("DONE")

for i in range(2,2**8,2):
    if i in combD:
        continue
    else:
        print(f"NO {i}") """

def isPower2(n):
    return bin(n).count('1')==1

ttt = int(input())
for _ in range(ttt):
    target = int(input())
    if target > 2**30 or target%2 > 0 or target <6 or isPower2(target):
        print(-1)
        continue

    ans = [0,1,target//2]
    while x(*ans) != target:
        ans[1]*=2
    print(*ans)