# https://www.codechef.com/COOK140C?order=desc&sortBy=successful_submissions

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def digitSumIsOdd(n):
    digits = list(str(n))
    oddCount = len([d for d in digits if int(d)%2>0])
    return oddCount%2>0

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    x = n+1
    np = digitSumIsOdd(n)
    while np == digitSumIsOdd(x):
        x+=1
    print(x)
