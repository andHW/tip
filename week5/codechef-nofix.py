# https://www.codechef.com/FEB222C/problems/NOFIX

ttt = int(input())

def calDist(aList):
    magics = [ i-x+1 for i, x in enumerate(aList) ]
    return magics

for _ in range(ttt):
    n = int(input())
    xs = list(map(int,input().split()))

    start = 0
    magics = calDist(xs)

    start = 0
    for m in magics:
        if m == start:
            start-=1

    print(-start)