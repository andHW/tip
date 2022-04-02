# https://atcoder.jp/contests/abc246/tasks/abc246_c

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


n,k,x = map(int, input().split())
items = list(map(int, input().split()))


itemCouponedPrices = []
for i, item in enumerate(items):
    c_price = item%x
    kUsed = item//x
    diff = item - c_price
    itemCouponedPrices.append((diff, i))

itemCouponedPrices.sort(reverse=True)

print(items)
print(itemCouponedPrices)
res = sum(items) - sum([d for d, i in itemCouponedPrices[:k]])

print(res)