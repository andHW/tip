# https://atcoder.jp/contests/abc246/tasks/abc246_a

import sys

debug = False
# debug = True

points = 3

xs = set()
ys = set()
xys = set()
for _ in range(points):
    x,y = map(int, input().split())
    xys.add((x,y))
    xs.add(x)
    ys.add(y)

for x in xs:
    for y in ys:
        p = (x,y)
        if p not in xys:
            print(*p)
            break
