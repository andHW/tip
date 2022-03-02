# https://www.codechef.com/START28C/problems/CARCHOICE

debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    x1,x2,y1,y2 = map(int,input().split())
    cost1 = y1/float(x1)
    cost2 = y2/float(x2)

    # print(cost1, cost2)

    diff = cost1 - cost2
    if diff > 0:
        diff = 1
    elif diff <0:
        diff = -1
    else: diff = 0
    
    print(diff)