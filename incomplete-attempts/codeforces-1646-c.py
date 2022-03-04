# https://codeforces.com/contest/1646/problem/C

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


powerfuls = set()

i = 2
while i <= 10**12:
    powerfuls.add(i)
    i *= 2

f = 1
i = 2
while f <= 10**12:
    powerfuls.add(f)
    f *= i
    i += 1

powerfuls = list(powerfuls)
powerfuls.sort()
print(powerfuls)
print(len(powerfuls))

ttt = int(input())
for _ in range(ttt):
    n = int(input())
