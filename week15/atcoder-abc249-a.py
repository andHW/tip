# https://atcoder.jp/contests/abc249/tasks/abc249_a

import sys
import math

# debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def dist(speed, duration, rest, sec):
    # x = sec
    # secRunning = x//(duration+rest)*duration + min(duration, x%(duration+rest))
    dist = 0
    while sec:
        if sec >= duration+rest:
            dist += speed*duration
            sec -= duration+rest
            continue
        dist += speed*min(duration, sec)
        sec = 0
    return dist

a,b,c,d,e,f,x = map(int, input().split())

taka = dist(b, a, c, x)

aoki = dist(e, d, f, x)

dprint(taka)
dprint(aoki)

if taka == aoki:
    print("Draw")
elif taka > aoki:
    print("Takahashi")
else:
    print("Aoki")