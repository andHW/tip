# https://www.codechef.com/START26C/problems/SMOKE
"""
🌿🌿🌿420🌿🌿🌿

emission = aX + bY
N <= 100*a + 4*b
a>=0, b>=0
2 unknowns: a and b
2 equations

100*a >= N-4*b
a >= (N-4*b)/100

emission = X*(N-4*b)/100 + bY
         = (XN - X4b)/100 + bY
         = (XN - X4b +100bY)/100
         minimize b

@!$#%^&$%#^$&%^ Started too late :(

"""

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n, x, y = map(int, input().split())
    emission=0

    print(n,x,y)

    print(f"x/100:{x/100}")
    print(f"y/4:{y/4}")
    print(f"n//100:{n//100}")
    print(f"n//4:{n//4}")

    if 100/x < 4/y:
        emission+=(1+n//100)*x
        n-= ( 1+n//100 )*100
    else:
        emission+=n//4*y
        n%= ( 1+n//4 )*4
    
    print(f"wtf:{emission}")

    if n:
        if x<y:
            emission+=x
        else:
            emission+=y



    print(emission)

