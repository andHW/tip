# https://www.codechef.com/START33C/problems/DISTDILEM

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
    arr = list(map(int, input().split()))

    asum = sum(arr)
    ans = 0
    i = 1
    while asum > 0:
        if asum >= i:
            asum -= i
            ans += 1
        else:
            break
        i+=1
    print(ans)
