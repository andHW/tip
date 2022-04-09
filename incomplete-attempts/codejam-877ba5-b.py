# PROBLEM_LINK

import sys
import math
from itertools import permutations, combinations

from numpy import half

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

"""
upBound = 10
mine = [10,9,8,7]
sMine = sum(mine)

numLeft = list(set(range(1,upBound+1))-set(mine))
print(mine)
print( numLeft )

can = 0
numOfCombs = 0
combs = combinations(numLeft, 4)
for comb in combs:
    numOfCombs+=1
    found = False
    newList = mine+list(comb)
    for ci in range(1, len(newList)//2+1):
        for cb in combinations(newList, ci):
            leftSum = sum(cb)
            rightList = list(set(newList)-set(cb))
            rightSum = sum(rightList)
            if leftSum ==rightSum:
                found = True
                print("FOUND!")
                print(cb)
                print(rightList)
    if found:
        # print(comb)
        can +=1
print(f"{can}/{numOfCombs}")
        

print("done")
"""
ttt = int(input())

maxAi = 10

for t in range(ttt):
    # print(f"Case #{t+1}:")
    n = int(input())
    myAs = list(range(maxAi,maxAi-n,-1))
    bs = list(map(int, input().split()))

    newList = myAs + bs
    dprint(newList)
    halfSum = sum(newList)//2
    dprint(halfSum)

    # knapsack
    dp = [0]*(halfSum+1)
    dp[0] = halfSum
    prevItem = [0]*(halfSum+1)
    for num in newList:
        for i in range( halfSum, 0, -1):
            if i >= num:
                dp[i] |= dp[i-num]
                prevItem[i] = num
        dprint(dp)
    ans = []
    tempSum = halfSum
    while tempSum > 0:
        ans.append(prevItem[tempSum])
        tempSum -= prevItem[tempSum]
    print(ans)
