# https://www.codechef.com/COOK140C/problems/RECSTI

from collections import defaultdict
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    ls = list(map(int, input().split()))

    counter = defaultdict(int)
    for l in ls:
        counter[l] += 1
    
    pairs = 0
    ans = 0
    for l in counter:
        c = counter[l]
        pairs += (c+c%2)//2
        ans+=c%2
    ans += pairs%2
    if n < 4:
        ans = 4-n
    print(ans)
