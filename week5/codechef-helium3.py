# https://www.codechef.com/FEB222C/problems/HELIUM3

ttt = int(input())

for _ in range(ttt):
    a,b,x,y = map(int,input().split())
    ok = x*y >= a*b
    if ok:
        print("Yes")
    else:
        print("No")