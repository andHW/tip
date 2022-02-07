# https://codeforces.com/contest/1634/problem/C
"""
n=2, k=3
1 3 5
2 4 6

n=2, k=4
1 3 5 7
2 4 6 8

n=4, k=2
1 5
2 6
3 7
4 8

n=3, k=2
1 5
2 4
3 6

n=3, k=4
1 5 7 11
2 4 8 10
3 6 9 12
"""
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    ok = False
    if n %2 <1:
        ok = True
    if k==1:
        ok = True
    if not ok:
        print("NO")
    else:
        print("YES")
        wow = [[0]]*n
        for i in range(1, n*k+1):
            wow[ (i-1)%n ].append(i)
        
        for row in wow:
            print(*row)


