# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33e95

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for ti in range(1,ttt+1):
    n = int(input())
    rows=[]
    iCount = 0
    for i in range(2*n):
        row = list(input())
        rows+=[row]
        iCount += row.count('I')

    for r in rows:
        dprint(r)

    top=btm=left=right=0
    for i in range(n):
        top+=rows[i].count("I")
        # btm+=rows[i+n].count("I")
        btm = iCount-top

    for i in range(2*n):
        left+=rows[i][:n].count("I")
        # right+=rows[i][n:].count("I")
        right = iCount-left


    res = 0
    oState = (top,left,btm,right,0)
    visited = set()
    bfsQueue = [oState]
    while bfsQueue:
        state = bfsQueue.pop(0)
        if state in visited:
            continue

        visited.add(state)

        t,l,b,r,c = state

        if t==l==b==r:
            res = c
            break

        # switching all on/off is easier
        if c >= iCount or c>= (n*2)**2:
            res = min(iCount, (n*2)**2)
            break
        
        # four possible moves: top/left top/right btm/left btm/right
        if top<n*2:
            bfsQueue+=[(t+1,l+1,b,r,c+1)]   # top/left
            bfsQueue+=[(t+1,l,b,r+1,c+1)]   # top/right
        if top>0:
            bfsQueue+=[(t-1,l-1,b,r,c+1)]   # top/left
            bfsQueue+=[(t-1,l,b,r-1,c+1)]   # top/right
        if btm<n*2:
            bfsQueue+=[(t,l+1,b+1,r,c+1)]   # btm/left
            bfsQueue+=[(t,l,b+1,r+1,c+1)]   # btm/right
        if btm>0:
            bfsQueue+=[(t,l-1,b-1,r,c+1)]   # btm/left
            bfsQueue+=[(t,l,b-1,r-1,c+1)]   # btm/right


    dprint(top,btm,left,right)
    
    print(f"Case #{ti}: {res}")