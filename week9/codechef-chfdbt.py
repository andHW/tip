# https://www.codechef.com/MARCH221C/problems/CHFDBT
"""
n=0 0
n=1 1
n=2 1
n=3 2
n=4 2
n=5 3
n=6 3
n=7 4
n=8 4
n=9 5
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
    print( n//2+(n%2>0) )

