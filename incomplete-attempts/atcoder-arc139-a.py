# PROBLEM_LINK

from hashlib import new
import sys
import math

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


n = int(input())

ts = map(int, input().split())

lv = -1
lt = 0
for t in ts:
    newAzs = max([t,lt,1])
    newAB = newAzs
    newA = int(newAB)

    dprint("newA:", newA)

    if newA <= lv:
        nonZeroPart = bin(lv)[2:].rstrip('0')
        if not nonZeroPart:
            nonZeroPart = "0"
        dprint(f"nonZeroPart {nonZeroPart}")
        magic = 1+int(nonZeroPart)
        dprint(f"magic: {magic}")
        dprint(f"newAzs: {newAzs}")
        magic = bin(magic)[2:]+(newAzs*"0")
        newA = int(magic)
    
    lt = t
    lv = newA

    print(f"lv {lv} lt {lt}")
print(lv)