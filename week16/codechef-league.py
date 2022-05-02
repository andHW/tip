# https://www.codechef.com/COOK141C/problems/LEAGUE
"""
<A>: win all
<B C D E>: ???
        B C D E
B-C:    1
B-D:    1   1
B-E:    1   1 1
C-D:    1 1 1 1
C-E:    1 2 1 2
D-E:    1 2 2 2
12-2*3 = 6
"""
import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n = int(input())
    winnerScore = (n-1) * 3
    losers = n-1
    loserGames = losers*(losers-1)//2
    sndScore = math.ceil(loserGames/losers)*3
    dprint(winnerScore, loserGames, losers, sndScore)
    print(winnerScore - sndScore)
