# https://www.codechef.com/COMA2022/problems/AGECAT1

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
    ans = ""

    if n >=1 and n<=18:
        ans = "Children"
    elif n>=19 and n<=55:
        ans = "Citizens"
    else:
        ans = "Senior Citizens"


    print(ans)
