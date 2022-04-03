# https://www.codechef.com/COMA2022/problems/XORPAIR

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
    x = int(input())

    ans = 0
    for i,a in enumerate(arr):
        index = arr.find(a^n)
        if a^n in arr and index != i:
            del arr[index]
            continue
        ans+=1
    print(ans)
