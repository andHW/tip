# https://codeforces.com/contest/1634/problem/A
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    isP = True
    for i in range( len(s)//2 ):
        if s[i] != s[-i-1]:
            isP = False
            break
    
    if isP or k<1:
        print(1)
    else:
        print(2)
