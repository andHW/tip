# https://www.codechef.com/LTIME105C/problems/MOVIE2X

debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

x,y = map(int,input().split())
ans = y//2 + (x-y)
print(ans)