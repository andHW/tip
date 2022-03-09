# https://www.codechef.com/START29C/problems/BOMBTHEBASE

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n, x = map(int, input().split())
    hs = map(int, input().split())

    ans = 0
    for i, h in enumerate(hs):
        if h < x:
            ans = i + 1
    print(ans)
