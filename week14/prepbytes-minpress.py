# https://mycode.prepbytes.com/contest/MARATHONAPR22/problems/MINPRESS

"""
UUUD
1234
1->{2,3,4}: 1*3 = 3
4->{1,2,3}: 1*3 = 3
2->{3,4}  : 1*2 = 2
2->{1}    : 2*1 = 2
3->{4}    : 1*1 = 1
3->{1,2}  : 2*2 = 4
"""

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


# ttt = int(input())
ttt = 1

for _ in range(ttt):
    uds = list(input())

    ans = 0
    for i in range(len(uds)):
        ud = uds[i]
        if ud == 'U':
            ans += 2*i + 1*(len(uds)-i-1)
        else:
            ans += 1*i + 2*(len(uds)-i-1)

    print(ans)
