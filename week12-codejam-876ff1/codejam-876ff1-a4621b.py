# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

ttt = int(input())

for t in range(ttt):
    print(f"Case #{t+1}:")

    r, c = map(int, input().split())
    rowE = "-".join('+'*(c+1))
    rowO = ".".join('|'*(c+1))

    empty = ".."
    print(empty + rowE[2:])
    print(empty + rowO[2:])

    for i in range(r-1):
        print(rowE)
        print(rowO)
    print(rowE)
