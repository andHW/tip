# https://codeforces.com/contest/1650/problem/A

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    s = input()
    c = input()
    possibleCs = s[0:len(s):2]
    if c in possibleCs:
        print("YES")
    else:
        print("NO")
