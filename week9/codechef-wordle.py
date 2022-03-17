# https://www.codechef.com/MARCH221C/problems/WORDLE

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    s = input()
    t = input()
    a = [ "BG"[q==w] for q,w in zip(s,t) ]
    print("".join(a))