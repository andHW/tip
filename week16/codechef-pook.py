# https://www.codechef.com/COOK141C/problems/POOK
"""
1: 1
2: 1
3: 2
xox
xxp
pxx

4: 4
xxpx
pxxx
xxxp
xpxx

5: 5
xxxpx
xpxxx
xxxxp
xxpxx
pxxxx

6: 6
xpxxxx
xxxpxx
xxxxxp
xxxxxx
xxxxpx
pxxxxx
"""


def ans(n):
    if n < 3:
        return 1
    if n == 3:
        return 2
    return n


ttt = int(input())

for _ in range(ttt):
    n = int(input())

    print(ans(n))
