# https://www.codechef.com/START29C/problems/STRP

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = input()
    t = input()

    p = t[0]
    ans = 1
    for c in t[1:]:
        if c == p:
            p = None
            continue
        ans += 1
        p = c

    print(ans)
