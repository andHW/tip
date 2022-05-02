class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        res = number
        maxV = 0
        for i,c in enumerate(number):
            if c == digit:
                newNum = number[:i]+number[i+1:]
                newNumV = int(newNum)
                print(newNumV)
                if newNumV > maxV:
                    print("found")
                    maxV = newNumV
                    res = newNum
        return res