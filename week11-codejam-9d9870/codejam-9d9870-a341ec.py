# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a341ec

import sys

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for ti in range(1, ttt+1):
    mlxs = []    # m = arrivalTime, l = amount, x = expireTime
    d,n,u = map(int, input().split())
    for i in range(d):
        m, l, e = map(int, input().split())
        mlx = (m, l, m+e)
        mlxs.append(mlx)

    dprint(mlxs)

    mLen = len(mlxs)
    mlxi = 0
    res = 0
    os = map(int, input().split())
    for o in os:
        basilNeeded = u
        while mlxi<mLen and mlxs[mlxi][0] <= o:
            m,l,x = mlxs[mlxi]
            
            spoiled = x <= o
            used = l <= 0
            if spoiled or used:
                mlxi+=1
                continue

            if l > basilNeeded:
                l -= basilNeeded
                mlxs[mlxi] = (m,l,x)
                basilNeeded = 0
                break
            else:
                basilNeeded -= l
                mlxi+=1
                continue
        
        fulfilled = basilNeeded <= 0
        if not fulfilled:
            break
        else:
            res+=1

    print(f"Case #{ti}: {res}")