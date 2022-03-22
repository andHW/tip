# https://mycode.prepbytes.com/contest/MARATHONMAR22/problems/ONEDSTRG1
"""
Crappy problem with crappy test cases.
Their input has nonumeric characters.
"""
import sys
import re

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    trash_input = input()
    dprint( "*"+trash_input+"*" )
    if "-" in trash_input:
        while True: pass
    normal_input = re.sub('[^0-9]','', trash_input)
    ss = set(list(normal_input))
    ss = list(ss)
    ss.sort()

    dprint(ss)

    possible = "1"
    for i in range(1,len(ss)):
        if int(ss[i]) - int(ss[i-1]) > 1:
            possible = "0"
            break

    print(possible+"D")