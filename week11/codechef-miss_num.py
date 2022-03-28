# https://www.codechef.com/MARCH222C/problems/MISS_NUM

"""
a+b = sum
a-b = diff
sum+diff = a+b+a-b  = 2a

since idk which ones are the sum and diff,
brute force on 4C2 combinations

BEWARE OF THE A,B CONSTRAINTS: [1,10^4]
!@$#%@$^@%#@$^#%&$*^&%#^$@%#^$#&%$*^&^$%@#^$#&%$
"""
import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


magic = {}

for i in range(1,1001):
    for j in range(1,1001):
        a = i+j
        b = i-j
        c = i*j
        d = i//j
        ij = [i,j]
        abcd = sorted([a,b,c,d])
        magic[tuple(abcd)] = ij


def findAB(qwer):
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
            mySum = qwer[i]
            diff = qwer[j]
            if (mySum+diff)%2>0:
                continue
            
            ta = (mySum+diff)//2
            tb = mySum - ta

            if ta<1 or ta>10**4:
                continue
            if tb<1 or tb>10**4:
                continue

            annoyingProduct = 0
            if tb!=0:
                annoyingProduct = ta//tb

            sdpd = qwer[:]
            sdpd.remove(mySum)
            sdpd.remove(diff)
            pOrD = sorted(sdpd)
            tatbPD = sorted([ta*tb, annoyingProduct])
            if pOrD==tatbPD:
                return (ta,tb)

    return (-1,-1)


# for i in range(1,1001):
#     for j in range(1,1001):
#         a = i+j
#         b = i-j
#         c = i*j
#         d = i//j

#         abcd = sorted([a,b,c,d])
#         myFind = findAB(abcd) 
#         if myFind != (i,j):
#             print("OH NO!!!!!!!!!!!")
#             print(f"myFind: {myFind}")
#             print(i,j)
#             print(a,b,c,d)
# dprint("WELL DONE!")

ttt = int(input())
for _ in range(ttt):
    abcd = list(map(int, input().split()))

    found = False
    a,b = findAB(abcd)
    
    print(*[a,b])