# https://www.codechef.com/FEB221C/problems/EUREKA

t = int(input())
for _ in range(t):
    n = int(input())
    res = round( (0.143*n)**n )
    print(res)