# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7

from collections import defaultdict
import sys

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    fs = list(map(int, input().split()))
    ps = list(map(int, input().split()))

    dists = defaultdict(dict)
    nodeWithParents = set()
    for i, (f, p) in enumerate(zip(fs, ps)):
        nodeWithParents.add(p)
        dists[p][i+1] = f
        dists[i+1][p] = f
    dprint(dists)
    dprint(nodeWithParents)

    # must be dijkstra but I got too much work to do 🥲
