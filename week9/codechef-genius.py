# https://www.codechef.com/MARCH221C/problems/GENIUS

"""
a+b <= n
a>=0
b>=0
3a-b = x
a,b,c are integer

b = 3a-x
a = (x+b)/3

a+3a-x <= n
4a-x <= n
4a <= n+x

x+b+3b <= 3n
x+4b <= 3n
4b <= 3n-x

4a <= n+x
4b <= 3n-x
a >= 0
b >= 0
3a-b = x
3a = x+b

"""
debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    n, x = map(int, input().split())
    aUpperBound = (n+x)//4
    bUpperBound = (3*n-x)//4

    ok = False
    for b in range(bUpperBound+1):
        ok = (x+b) % 3 == 0
        if ok:
            a = (x+b)//3
            print("YES")
            print(*[a, b, n-a-b])
            break

    if not ok:
        print("NO")
