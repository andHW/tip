
# https://www.codechef.com/FEB222C/problems/XORPAL
"""
one=1 || zero=1 length = even -> False
one==zero -> True
00000111
11111000
"""
import itertools


def isXorPal(s):
    ns = [ int(c) for c in s ]
    baseVal = ns[0] ^ ns[-1]
    for i in range( 1, len(s)//2 ):
        if ns[i]^ns[-i-1] != baseVal:
            return False
    return True

# for one in range(1,4):
#     for zero in range(1,10):
#         ps = list( itertools.permutations( ['0']*zero+['1']*one ) )
#         possible = False
#         for p in ps:
#             sss = "".join(p)
#             if isXorPal(sss):
#                 possible = True
#                 break
#         print(f"one:{one}\tzero:{zero}\t{possible}")

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    s = input()
    ones = s.count('1')
    zeros = len(s) - ones

    ok = len(s)%2>0 or ones*zeros==0 or ones==zeros
    if not ok:
        # must be even number
        ok = ones%2==0

    if ok:
        print("YES")
    else:
        print("NO")
