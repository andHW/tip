# https://mycode.prepbytes.com/contest/MARATHONMAR22/problems/TREMAG

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def dfsFindEdgeFreq(src, parent, tree, edges):
    dprint("dfsFindEdgeFreq")
    freq = 1
    for n in tree[src]:
        dprint("n: %s \t src: %s \t parent: %s" % (n,src,parent))
        if n==parent:
            dprint("^skipped")
            continue
        subTreesFreq = dfsFindEdgeFreq(n, src, tree, edges)
        freq += subTreesFreq


    if src==parent:
        return
    
    edgeName = (src,parent)
    if src > parent:
        edgeName = (parent, src)
    edges[edgeName]["freq"] = freq
    dprint("------edges[{}]".format(edgeName))
    dprint(edges[edgeName])
    return freq


ttt = int(input())

for _ in range(ttt):
    *nc, src = input().split()
    n, c = map(int, nc)
    dprint(n, c, src)
    tree = {}
    edges = {}
    for i in range(n-1):
        a, b, w = input().split()
        if a > b:
            a, b = b, a
        w = int(w)

        if a not in tree:
            tree[a] = []
        if b not in tree:
            tree[b] = []

        tree[a].append(b)
        tree[b].append(a)
        edgeName = (a,b)
        if a>b:
            edgeName = (b,a)
        edges[edgeName] = {
            "weight": w,
            "freq": 0,
        }
        dprint(a, b, w)

    dprint(tree)

    """
    stack = [src]

    paths = {}
    for n in tree:
        paths[n] = []

    seen = set()
    while stack:
        dprint("-----stack-----")
        dprint(stack)
        top = stack.pop()
        seen.add(top)
        for node in tree[top]:
            a, b = top, node
            if node in seen:
                continue
            
            normEdge = (a,b)
            if a>b:
                normEdge = (b,a)

            paths[b] = paths[a]+[normEdge]
            stack.append(node)

    for p in paths:
        for e in paths[p]:
            edges[e]["freq"] += 1

    dprint("-----paths-----")
    for p in paths:
        dprint("{}: {}".format(p, paths[p]))
    """

    dfsFindEdgeFreq(src, src, tree, edges)

    dprint("-----edges-----")
    for e in edges:
        dprint("{}: {}".format(e, edges[e]))

    ewfs = []
    for eName in edges:
        e = edges[eName]
        wf = e["weight"]*e["freq"]
        ewf = (wf, eName)
        ewfs.append(ewf)

    ewfs.sort(reverse=True)
    for ewf in ewfs[:c]:
        _, eName = ewf
        edges[eName]["weight"] = 0

    dprint(ewfs)

    magic = sum([e["weight"]*e["freq"] for e in edges.values()])
    print(magic)
