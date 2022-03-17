# https://www.codechef.com/MARCH221C/problems/SUBSTRING

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    s = input()
    magicS = s.replace(s[0],s[-1])

    ans = 0
    substrings = magicS.split(s[-1])
    ans = max( [len(s) for s in substrings] )

    if ans == 0:
        ans = -1

    print(ans)
