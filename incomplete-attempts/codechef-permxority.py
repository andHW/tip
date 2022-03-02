# https://www.codechef.com/START28C/problems/PERMXORITY
import itertools
"""
length even case:

1 XOR 1 XOR 1 = 1

length odd case:
1 2 3 4 5
1-2 = 1
2-3 = 1
3-4 = 1
4-5 = 1
"""

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


def isAttractive(xs):
    absDiffs = [abs(i-j) for i, j in zip(xs, xs[1:])]
    xorsum = 0
    for d in absDiffs:
        xorsum ^= d
    return xorsum == 0


def tellIfIsAttractive(xs):
    dprint("Telling:")

    if isAttractive(xs):
        dprint("GOOD!")
    else:
        dprint("BAD!")


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    if n <= 2:
        # should reach here since 2<=n
        print(-1)
        continue

    ans = []
    if n % 2 == 0:
        a = list(range(1, n-2))
        b = [n] + list(range(n-2, n))
        ans = a+b
    else:
        ans = list(range(1, n+1))
    if ans == []:
        print(-1)
    else:
        print(*ans)
    # tellIfIsAttractive(ans)
