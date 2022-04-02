# https://atcoder.jp/contests/abc246/tasks/abc246_b
"""
             b
            /|
           / |
          /  |
         /   |
        /    |
     x /     |
    1 /|     |
     / |     |
    /  |     |
 o /___|_____| a

 length ob = sqrt(oa^2 + ob^2)
 length ox = 1
 here we have the ratio we want
"""
import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


a,b = map(int, input().split())
lenAb = math.sqrt( a**2 + b**2 )
ratio = 1/lenAb
print(*[ratio*a, ratio*b])