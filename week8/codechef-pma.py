# https://www.codechef.com/START29C/problems/PMA

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = input()
    xs = list(map(lambda x: abs(int(x)), input().split()))

    pves = xs[::2]
    nves = xs[1::2]
    dprint(pves, nves)

    pmin = min(pves)
    nmax = max(nves)

    if nmax > pmin:
        pi = pves.index(pmin)
        ni = nves.index(nmax)
        pves[pi], nves[ni] = nves[ni], pves[pi]
    
    dprint(pves, nves)

    ans = sum(pves)-sum(nves)
    print(ans)
