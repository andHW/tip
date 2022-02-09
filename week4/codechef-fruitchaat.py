# https://www.codechef.com/START25C/problems/FRUITCHAAT
ttt = int(input())

for _ in range(ttt):
    x,y = map(int,input().split())
    ans = min( x//2, y )
    print( ans )
