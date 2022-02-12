# https://codeforces.com/contest/1634/problem/B
"""
odd  + odd   = even
odd  + even  = odd
even + even  = even

odd  ^ odd   = even
odd  ^ even  = odd
even ^ even  = even
"""

def isOdd(n):
    return n%2 > 0 

t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))

    aliceIsOdd = isOdd(x)
    for elm in a:
        aliceIsOdd = isOdd(aliceIsOdd + elm)

    if aliceIsOdd == isOdd(y):
        print("Alice")
    else:
        print("Bob")

