# https://mycode.prepbytes.com/contest/PRIMETIMEAPR22/problems/NONPAL
"""

"The next T lines contain a single string of lowercase English alphabets" ???

This is misleading.
Shit problem and shit contest!!!

"""
def ans(s):
    if len(set(s)) <= 1:
        return "NO"
    return "YES"

ttt = int(input())

for _ in range(ttt):
    s = input()
    s = [c for c in s if c.islower()]   # this line is rediculous
    print(ans(s))
