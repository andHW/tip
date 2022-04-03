# https://leetcode.com/contest/biweekly-contest-75/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        print(bin(start),bin(goal))
        s1 = bin(start)[2:]
        s2 = bin(goal)[2:]
        
        maxLen = max(len(s1), len(s2))
        
        s1 = s1.zfill(maxLen)
        s2 = s2.zfill(maxLen)
        
        for c1, c2 in zip(s1,s2):
            if c1!=c2:
                ans+=1
        return ans