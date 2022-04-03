# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b

# I got two approachs, they have different good stuff.

def smoothArray1(arr, target):
    for i,c in enumerate(arr):
        if c >= target:
            arr[i] = target
            break
        arr[i] = c
        target -= c
    arr[i+1:] = [0] * (len(arr) - i - 1)
    return arr

def smoothArray2(arr, target):
    # doesn't need to rebuild the list, just change the values
    exceed = sum(arr) - target
    while exceed > 0:
        for i in range(len(arr)):
            if exceed == 0:
                break

            v = arr[i]
            if exceed > v:
                exceed -= v
                arr[i] = 0
            else:
                # need <= v
                arr[i] -= exceed
                exceed = 0
    return arr


ttt = int(input())

for t in range(ttt):
    print(f"Case #{t+1}: ", end="")
    cymkMin = [10**6]*4
    for i in range(3):
        cymk = map(int, input().split())
        for i, cV in enumerate(cymk):
            cymkMin[i] = min(cymkMin[i], cV)

    cSum = sum(cymkMin)
    if cSum >= 10**6:
        # smoothArray2(cymkMin, 10**6)
        # res = cymkMin
        res = smoothArray1(cymkMin, 10**6)
        print(*res)
    else:
        print("IMPOSSIBLE")
