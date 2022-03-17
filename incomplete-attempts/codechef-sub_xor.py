# https://www.codechef.com/MARCH221C/problems/SUB_XOR

debug = False
debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs)


ttt = int(input())

for _ in range(ttt):
    # n = input()
    s = input()

    ones = s.count('1')

    substrings = []
    slen = len(s)
    for i in range(slen+1):
        for j in range(slen+1):
            substrings.append(s[i:j])
    substrings = [s for s in substrings if s != '']
    nums = [int(s, 2) for s in substrings]
    nums.sort()
    nums = [str(n) for n in nums]
    res = eval('^'.join(nums)) % 998244353

    dprint("-----------------------")
    dprint(f"input:{s}")
    dprint(f"d:{int(s,2)}")
    dprint(substrings)

    # for substring in substrings:
    #     dprint(f"{substring.zfill(len(s)+1)}")
    dprint(f"{s.zfill(len(s)+1)} |  INPUT IN BINARY")
    dprint(f"{bin(res)[2:].zfill(len(s)+1)} |  RESULT IN BINARY")
    

    dprint(f"nums:{nums}")
    dprint(f"res:{res}")
    print(res)
