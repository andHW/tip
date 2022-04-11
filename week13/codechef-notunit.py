# https://www.codechef.com/APRIL221C/problems/NOTUNIT

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def getAns(a, b):
    if a % 2 < 1 and a+2 <= b:
        return (a, a+2)

    if a % 3 < 1 and b >= a+3:
        return(a, a+3)
    
    if a%2 > 0 and a+3 <= b:
        return (a+1, a+3)

    return [-1]


ttt = int(input())

for _ in range(ttt):
    a, b = map(int, input().split())
    ans = getAns(a, b)
    print(*ans)
    
    if len(ans)>1:
        dprint(f"gcd: {math.gcd(ans[0],ans[1])}")
