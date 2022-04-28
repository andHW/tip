# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d
"""
I thought you can only deque when you serve a customer in the competition.
From what I understand now, this restaurant is actually serving pancakes **for free** to customers.
I totally missed this point. 🤦🤦🤦🤦🤦🤦🤦🤦🤦🤦🤦
"""

ttt = int(input())

for t in range(ttt):
    n = int(input())
    ds = list(map(int, input().split()))

    left = 0
    right = n-1

    ans = 0
    delicious = 0

    while left <= right:
        ld = ds[left]
        rd = ds[right]

        served = False
        if ld <= rd:
            if ld >= delicious:
                delicious = ld
                served = True
            left += 1
        else:
            if rd >= delicious:
                delicious = rd
                served = True
            right -= 1

        if served:
            ans += 1

    ans = min(n, ans)

    print(f"Case #{t+1}: {ans}")
