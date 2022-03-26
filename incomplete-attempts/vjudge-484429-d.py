# https://vjudge.net/contest/484429#problem/D
"""
My brain is fucked 🤦.
Types: o, h, l, x

o  h   l  x1  x2  x3  x4

o  hh  l  qq  w   ee   r
       l  q   ww   e  rr

------------------------

oo oo hh ol lo ll hh or wo qq ee
oo hh oo ol lo ll hh rr ww qo oe

comb: 11 
o:    16
h/l:  8
qwer: 4

dp[1]=2    o h
           o h
           dp[1]*2
dp[2]=11   oo hh   | hh ol lo ll hh or wo qq ee
           oo hh   | oo ol lo ll hh rr ww qo oe

           dp[1]+dp[2]                           xxxxxxx
dp[3]=??   ooo ool olo oll loo lol llo lll ... | qqr wee
           ooo ool olo oll loo lol llo lll ... | qrr wwe

dp[4]=     dp[3]+dp[1] +dp[2]*2

oo hh hh qq ee qq qq
oo hh hh qr we qo ql
oo hh oo rr ww hh ol


"""
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    # n is the length of the walkways
    k, n = map(int, input().split())

