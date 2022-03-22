# https://mycode.prepbytes.com/contest/MARATHONMAR22/problems/COLBAL
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


n = int(input())
bs = map(int, input().split())
cs = list(input())

red = []
blue = []
for b, c in sorted(zip(bs, cs)):
    if c == 'B':
        if b >= 1:
            blue.append(b)
    else:
        if b < n+1:
            red.append(b)

dprint(red, blue)

possible = True
if len(red)+len(blue) < n:
    possible = False
else:
    for i in range(1, n+1):
        if blue and blue[0] >= i:
            blue = blue[1:]
        elif red and red[0] <= i:
            red = red[1:]
        else:
            possible = False
            break

if possible:
    print("YES")
else:
    print("NO")
