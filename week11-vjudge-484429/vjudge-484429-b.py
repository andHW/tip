# https://vjudge.net/contest/484429#problem/B

ttt = int(input())

for _ in range(ttt):
    k, b, n = map(int, input().split())
    ans = 0
    digits=[]
    while n>=b:
        digit = n%b
        digits+=[digit]
        ans += digit**2
        n//=b
    digits+=[n]
    ans += n**2
    print(*[k, ans])
    # print(digits[::-1])