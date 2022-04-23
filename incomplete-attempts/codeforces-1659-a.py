# https://codeforces.com/contest/1659/problem/A
"""
b=1
    r=2: RBR
    r=3: RBRR
    r=4: RRBRR
    r=5: RRRBRR
    r=10: RRRRRBRRRRR
b=2
    r=3: RBRBR
    r=4: RRBRRB
    r=5  RRBRRBR
    r=6  RRBRRBRR
    r=10 RRRBRRRBRRRR

b=4
    r=6: RRBRRBRRBB
RRBRRBRRBRRBRRBRRBR
"""
import sys
import math

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n, r, b = map(int, input().split())
    magic = math.ceil(r/b)
    dprint(n,r,b)
    dprint(magic)
    remainA = ["R"*(r-magic*b)]
    rs = ["R"*magic]*(b)+remainA
    ans = "B".join(rs)
    print(ans)

