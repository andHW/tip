# https://www.codechef.com/START33C/problems/MTE
"""
There must be a cleaner logic to solve this problem.
"""
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def countOddInArr(arr):
    oddCount = 0
    for a in arr:
        if a % 2 > 0:
            oddCount += 1
    return oddCount

# pattern searcher that is not used in the solution
def bfs(s):
    q = [(tuple(s),0,())]
    visited = set()
    visited.add(q[0])
    while q:
        top = list(q.pop(0))
        u = list(top[0])
        step = top[1]
        ancestors = list(top[2])
        oddCount = countOddInArr(u)
        evenCount = len(u) - oddCount

        if oddCount*evenCount == 0:
            print(ancestors)
            return step

        for i in range(len(u)):
            for j in range(i+1, len(u)):
                newElm = u[i] + u[j]
                newU = u[:]
                del newU[i]
                del newU[j-1]
                newU.append(newElm)
                q.append((tuple(newU), step+1, tuple(ancestors+[u])))
                # dprint(q)

    return -1

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    arr = list(map(int, input().split()))
    dprint(arr)

    # dprint(bfs([int(a) for a in arr]))

    oddCount = 0
    for a in arr:
        if a % 2 > 0:
            oddCount += 1
    evenCount = n - oddCount

    if n != len(arr):
        while True:
            print("WTF?")

    if oddCount*evenCount < 1:
        print(0)
        continue

    if oddCount == evenCount:
        # 6 9
        # 6 6 9 9
        # 6 6 6 9 9 9
        if oddCount % 2 < 1:
            print(oddCount//2)
            continue
        # 6 6 6 9 9 9
        print(n//2)
    elif oddCount > evenCount:
        # 6 9 9
        # 6 9 9 9
        # 6 6 9 9 9
        # 6 6 6 9 9 9 9
        if oddCount % 2 < 1:
            print( min(oddCount//2, evenCount) )
            continue
        print(evenCount)
        continue
    else:
        # evenCount > oddCount
        # 6 6 6 9 9
        if oddCount%2 < 1:
            print(oddCount//2)
            continue

        # 6 6 9
        # 6 6 6 9
        # 6 6 6 6 9 9 9
        print(evenCount)
