# https://dmoj.ca/problem/afd1p2

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

s1 = "chipmunk"
s2 = "pikcuhmn"

si1 = {c: i for i, c in enumerate(s1)}
si2 = {c: i for i, c in enumerate(s2)}

crazyMapping = [0]*8
for c in s1:
    crazyMapping[si2[c]] = si1[c]
print(crazyMapping)

s = input()
output = list(s)
for i in range(len(s)):
    output[i] = s[crazyMapping[i]]
print("".join(output))