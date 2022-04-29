# https://mycode.prepbytes.com/contest/PRIMETIMEAPR22/problems/LEXDIF

import sys
from itertools import permutations

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


n = int(input())

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

ps = sorted(permutations(p1))
magic = {}
for i, p in enumerate(ps):
    magic[p] = i

ans = abs(magic[tuple(p1)] - magic[tuple(p2)])

print( ans )