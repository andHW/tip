# https://www.codechef.com/START25C/problems/TOWERTOP
from math import log, ceil
ttt = int(input())

for _ in range(ttt):
    x, m = map(int, input().split())
    magic = ceil(log(x)/log(2)) + 1

    if magic > m:
        print(0)
    else:
        print(1+m-magic)
