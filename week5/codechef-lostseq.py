# https://www.codechef.com/START26C/problems/LOSTSEQ
"""
A = [a1, a2, a3]
B = [ a1+k1, a1-k1, a2+k2, a2-k2, a3+k3, a3-k3 ]
sum(A) = a1+a2+a3
sum(B) = 2a1+2a2+2a3

a1+k1+a1-k1 = 2a1

[2,10000000,1,1]
[1,5000001]
10000000 = 5000001+4999999
2        = 5000001-4999999
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
    bs = (map(int,input().split()))

    ok = sum(bs)%2==0

    if ok:
        print("YES")
    else:
        print("NO")