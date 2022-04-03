# https://www.codechef.com/COMA2022/problems/HAWKINTERN

from collections import defaultdict
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    s = input()
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    if counter['L'] == counter['R'] and counter['U'] == counter['D']:
        print("YES")
    else:
        print("NO")


