# https://www.codechef.com/MARCH221C/problems/CHFCLASS

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    print( n//7 + (n%7>=6) )
