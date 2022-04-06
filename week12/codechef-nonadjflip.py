# https://www.codechef.com/START33C/problems/NONADJFLIP

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    s = input()

    ans = 0
    if "11" in s:
        ans += 1
    s.replace("11","1")

    if "1" in s:
        ans += 1
    
    print(ans)
