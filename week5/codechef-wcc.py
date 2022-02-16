# https://www.codechef.com/FEB222C/problems/WCC

ttt = int(input())

for _ in range(ttt):
    x = int(input())
    line = input()

    cWin = line.count('C')
    nWin = line.count('N')

    coeffient = 1
    if cWin > nWin:
        coeffient = 60
    elif cWin < nWin:
        coeffient = 40
    else:
        coeffient = 55
    
    print( coeffient*x )

