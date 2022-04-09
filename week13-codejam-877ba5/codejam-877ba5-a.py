# PROBLEM_LINK

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for t in range(ttt):
    print(f"Case #{t+1}: ", end="")
    s = input()+'*'
    ans = ""

    sameCount = 0
    for i in range(len(s)-1):
        a,b = s[i:i+2]

        if a == b:
            sameCount += 1
            continue
        else:
            if sameCount > 0 and ord(a) < ord(b):
                ans += a*(sameCount+1)*2
                sameCount = 0
                continue
            elif sameCount > 0:
                ans += a*(sameCount+1)
                sameCount = 0
                continue

        if ord(a) < ord(b) and b != '*':
            ans += a*2
        else:
            ans += a
    print(ans)