# https://codeforces.com/contest/1646/problem/A
"""
(n-1)*(n+1) = n**2 - 1
a sequence without n**2 can never reach n**2
"""
debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n, s = map(int,input().split())
    ans = s//n**2
    print(ans)