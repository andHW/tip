# https://codeforces.com/contest/1673/problem/C
"""
1 (1): 1
2 (2): 1+1, 2
3 (3): 1+1+1, 2+1, 3
4 (5): 1+1+1+1, 2+1+1, 3+1, 2+2, 4
5 (7): 1+1+1+1+1, 2+1+1+1, 3+1+1, 4+1, 5, 2+2+1, 3+2
6 (11): 1+1+1+1+1+1, 2+1+1+1+1, 3+1+1+1, 4+1+1, 5+1, 6, 2+2+1+1, 2+2+2, 3+2+1, 4+2

"""
import sys
import math

debug = False
# debug = True


q = { 1: [[1]] }
def decompose(n):
    try:
        return q[n]
    except:
        pass
    result = [[n]]

    for i in range(1, n):
        a = n-i
        R = decompose(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)
    q[n] = result
    return result


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

ll = 0
for i in range(1, 12):
    l = len(decompose(i))
    print(f"{i} {l} {l-ll}")
    ll = l

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    print()
