# https://www.codechef.com/submit/DCP

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


n, m = map(int, input().split())
qs = list(map(int, input().split()))

rules = {}

for i in range(m):
    ci, xi = map(int, input().split())
    wcs = list(map(int, input().split()))
    wcs = [wcs[i:i+2] for i in range(0, len(wcs), 2)]
    rules[ci] = wcs

dprint(rules)
dprint("")

hasNewCompound = True
while hasNewCompound:
    hasNewCompound = False
    for r in rules:
        qAmount = qs[r-1]
        if qAmount > 0:
            hasNewCompound = True
            wcs = rules[r]
            dprint(wcs)

            for w, c in wcs:
                qs[c-1] += qAmount*w
            qs[r-1] = 0
            dprint(qs)

for q in qs:
    print(q%(10**9+7))
