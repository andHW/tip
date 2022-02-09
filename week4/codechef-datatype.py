# https://www.codechef.com/START25C/problems/DATATYPE

ttt = int(input())

for _ in range(ttt):
    n, x = map(int, input().split())
    print(x % (n+1))