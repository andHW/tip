# https://codeforces.com/contest/1673/problem/A

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def s2score(s):
    return sum(ord(c) - ord('a') + 1 for c in s)

ttt = int(input())

for _ in range(ttt):
    s = input()
    if len(s) == 1:
        print(f"Bob {s2score(s)}")
        continue

    if len(s) % 2 < 1:
        print(f"Alice {s2score(s)}")
        continue

    as1 = s[1:]
    bs1 = s[0]

    as2 = s[:-1]
    bs2 = s[-1]

    s1s = s2score(as1) - s2score(bs1)
    s2s = s2score(as2) - s2score(bs2)

    print(f"Alice {max(s1s,s2s)}")
