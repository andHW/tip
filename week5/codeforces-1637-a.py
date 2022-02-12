# https://codeforces.com/contest/1637/problem/0

"""
What a lame statement.
Full of double negations.
"""

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

    lmax=[]
    cm = 0
    for x in xs:
        if x>cm:
            cm = x
        lmax.append(cm)
    
    rmin=[]
    cm = float('inf')
    for x in reversed(xs):
        if x<cm:
            cm = x
        rmin.append(cm)

    rmin.reverse()

    lmax = lmax[:-1]
    rmin = rmin[1:]

    allCanSort = True

    dprint(xs)
    for l,r in zip(lmax, rmin):
        # dprint(f'{l}:{r}')
        if l>r:
            allCanSort = False
            break

    if not allCanSort:
        dprint("not allCanSort")
        print("YES")
    else:
        dprint("allCanSort")
        print("NO")