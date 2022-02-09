#https://www.codechef.com/START25C/problems/POLIN
ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = set()
    ys = set()
    for _ in range(n):
        x,y = map(int,input().split())
        xs.add(x)
        ys.add(y)
    print( len(xs) + len(ys) )