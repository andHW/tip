# https://codeforces.com/contest/1637/problem/C

"""

01180
01261
02062
10063
... x 3
40036

011160
011241
012042
020043

0211110
1021110
2002110

0012100
1020100
2000200
3000001

0020200
1000201
2000002

00500
01310
02120
10220
20021
30002

0300
1101 X

0330
1140
1221
2022
3003

0500
1310
2120
2201
3002

0310
1120
1201
2002
"""
debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = list(map(int,input().split()))

    xs = xs[ 1:-1 ]

    if len(xs)==1 and xs[0]%2>0:
        print(-1)
        continue

    operations=0
    evens=0


    
    print(operations)
