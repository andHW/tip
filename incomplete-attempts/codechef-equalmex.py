# https://www.codechef.com/START25C/problems/EQUALMEX
from collections import Counter

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    xs = list(map(int,input().split()))


    ok = True

    counter = Counter(xs)
    for i in sorted(counter.elements()):
        if counter[i] == 1 or counter[i] > n:
            ok = False
            break
    
    if ok:
        print("YES")
    else:
        print("NO")