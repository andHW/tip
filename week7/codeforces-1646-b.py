# https://codeforces.com/contest/1646/problem/B

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = list(map(int, input().split()))
    xs.sort(reverse=True)
    dprint(xs)

    ok = False

    sumLeft = 0
    sumRight = xs[-1]

    halfI = len(xs)//2
    for i in range(halfI):
        sumLeft += xs[i]
        sumRight += xs[-i-2]
        if sumLeft > sumRight:
            ok = True
            break

    if ok:
        print("YES")
    else:
        print("NO")
