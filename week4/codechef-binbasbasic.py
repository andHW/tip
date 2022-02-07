# https://www.codechef.com/FEB221C/problems/BINBASBASIC

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    min_operations = 0

    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            min_operations += 1

    hasEnoughOperation = k >= min_operations
    canWasteOperation1 = (k-min_operations) % 2 < 1
    canWasteOperation2 = n % 2 > 0
    ok = hasEnoughOperation and (canWasteOperation1 or canWasteOperation2)
    
    if ok:
        print("YES")
    else:
        print("NO")
