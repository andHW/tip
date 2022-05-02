# https://www.codechef.com/COOK141C/problems/DOUBLEDDIST

import sys
import math

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
    arr.sort()

    ok = True
    for i in range(1, len(arr)-1):
        left = arr[i] - arr[i-1]
        right = arr[i+1] - arr[i]
        c1 = left == 2*right
        c2 = 2*left == right
        if not c1 and not c2:
            ok = False
            break
            
    if ok:
        print("Yes")
    else:
        print("No")