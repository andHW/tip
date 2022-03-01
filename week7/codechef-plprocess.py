# https://www.codechef.com/LTIME105C/problems/PLPROCESS

debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = list(map(int,input().split()))

    p1Stack = 0
    p2Stack = sum(xs)
    minTime = p2Stack
    for x in xs:
        p1Stack+=x
        p2Stack-=x
        newTime = max( p1Stack, p2Stack )
        if newTime < minTime:
            minTime = newTime
    print(minTime)