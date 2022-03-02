# https://www.codechef.com/START28C/problems/SUNDAY
"""
MO TU WE TH FR SA SU
01 02 03 04 05 06 07
08 09 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    holidays = set([6, 7, 13, 14, 20, 21, 27, 28])
    xs = set(map(int, input().split()))
    holidays.update(xs)
    print(len(holidays))