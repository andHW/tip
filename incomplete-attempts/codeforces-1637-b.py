# https://codeforces.com/contest/1637/problem/B

debug = False
debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = map(int,input().split())