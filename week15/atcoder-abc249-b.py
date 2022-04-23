# https://atcoder.jp/contests/abc249/tasks/abc249_b

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def ans(s):
    if not any(c.isupper() for c in s):
        return "No"
    
    if not any(c.islower() for c in s):
        return "No"
    
    # pairwise??? wtf?
    # for a,b in zip(s, s[1:]):
    #     if a==b:
    #         return "No"

    for c in set(s):
        if s.count(c) > 1:
            return "No"
    
    return "Yes"


s = input()

print(ans(s))