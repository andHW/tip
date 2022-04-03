# https://leetcode.com/contest/weekly-contest-287/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch,cm = map(int,current.split(":"))
        th,tm = map(int,correct.split(":"))
        
        cur = ch*60 + cm
        target = th*60 + tm
        diff = abs(target-cur)
        ans = 0
        while diff >0:
            ans+=1
            
            for t in [60,15,5,1]:
                if diff >= t:
                    diff -=t
                    break
        
        return ans