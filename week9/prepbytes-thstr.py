# https://mycode.prepbytes.com/contest/MARATHONMAR22/problems/THSTR

from collections import defaultdict
import sys
import math


debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def nCr(n, r):
    num = math.factorial(n)
    den = math.factorial(r) * math.factorial(n-r)
    return num//den

ttt = int(input())

for _ in range(ttt):
    n = int(input())

    counter = {}
    for _ in range(n):
        s = input()
        if s=="":
            continue
        f = s[0]
        if f in "APRIL":
            if f not in counter:
                counter[f] = 0
            counter[f] += 1
    
    if n<3:
        print(0)
        continue

    dprint(counter)

    counterSum = sum([counter[c] for c in counter])

    if counterSum < 3:
        print(0)
        continue

    ways = nCr(counterSum, 3)

    for c in "APRIL":
        if c not in counter:
            continue
        if counter[c] <=1:
            continue

        cCount = counter[c]
        extraWays = nCr(cCount,2)*(counterSum-cCount)
        if cCount>2:
            extraWays+=nCr(cCount,3)

        ways -= extraWays


    print(ways)