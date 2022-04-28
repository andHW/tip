# https://www.codechef.com/APRIL222C/problems/SST
ttt = int(input())

for _ in range(ttt):
    a, b = map(int, input().split())
    if a*2 == b:
        print("ANY")
    elif a*2 > b:
        print("FIRST")
    else:
        print("SECOND")
