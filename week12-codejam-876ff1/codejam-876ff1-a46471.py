# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
ttt = int(input())

for t in range(ttt):
    print(f"Case #{t+1}: ", end="")
    n = int(input())
    ss = list(map(int, input().split()))

    ss.sort()

    count = 0
    for s in ss:
        if s>count:
            count +=1
    print(count)
