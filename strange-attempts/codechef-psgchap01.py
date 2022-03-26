# https://www.codechef.com/ALGM2022/problems/PSGCHAP01
# Umm... This contest is no longer accessiable... Stragnge...
# My solution got a runtime error anyway...

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


a,b = map(int, input().split())
if a==b:
    print("Draw")
elif a>b:
    print("Vinith")
else:
    print("Deva")
