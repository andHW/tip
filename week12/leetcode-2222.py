# https://leetcode.com/contest/biweekly-contest-75/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        # the sliding windows
        numOfOnes = [0]*len(s)
        numOfOnes[0] = 1*(s[0]=='1')
        
        numOfZeros = [0]*len(s)
        numOfZeros[0] = 1-numOfOnes[0]

        for i in range(1, len(s)):
            numOfOnes[i] = numOfOnes[i-1] + (1*(s[i]=='1'))
            numOfZeros[i] = i+1-numOfOnes[i]

        res = 0
        for i in range(1, len(s)-1):
            if s[i] == '1':
                leftZeros = numOfZeros[i-1]
                rightZeros = numOfZeros[len(s)-1] - numOfZeros[i]
                olo = leftZeros * rightZeros
                res += olo
            else:
                leftOnes = numOfOnes[i-1]
                rightOnes = numOfOnes[len(s)-1] - numOfOnes[i]
                lol = leftOnes * rightOnes
                res += lol
        return res