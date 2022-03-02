# https://www.codechef.com/START28C/problems/SELFDEF

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = map(int, input().split())
    ans = sum(1 for x in xs if x >= 10 and x <= 60)
    print(ans)
