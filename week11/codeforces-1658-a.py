# https://codeforces.com/contest/1658/problem/A
"""
000

0110110

001

01101

10001
101001

1010101

001
0101
10101

01010101010101


"""
import sys
import re

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    sLen = int(input())
    s = input()
    on9 = s

    while "00" in on9 or "010" in on9:
        on9 = on9.replace("00","0110")
        on9 = on9.replace("010","0110")

    ans = len(on9)-len(s)
    # print(on9)
    print(ans)
