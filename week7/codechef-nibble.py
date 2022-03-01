# https://www.codechef.com/LTIME105C/problems/NIBBLE

debug = False
# debug = True

def dprint(*args, **kwargs):
    if not debug:
        return
    print( "debug:\t"+" ".join(map(str,args)), **kwargs )

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    if n%4 !=0:
        print("Not ",end="")
    print("Good")