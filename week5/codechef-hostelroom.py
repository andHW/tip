# https://www.codechef.com/START26C/problems/HOSTELROOM

debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n,x = map(int,input().split())

    ans = x
    for a in map(int,input().split()):
        x += a
        ans = max( x, ans )
    print(ans)