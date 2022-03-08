# https://codeforces.com/contest/1650/problem/B

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())


def f(x, a):
    return x//a + x % a


for _ in range(ttt):
    l, r, a = map(int, input().split())
    res = f(r, a)
    if a == r:
        res = max(res, f(a-1, a))
    elif l > a:
        for i in range(r, r-a-1, -1):
            if i<l: break
            newRes = f(i, a)
            if newRes > res:
                res = newRes
                break

    print(res)
