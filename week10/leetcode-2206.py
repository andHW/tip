# https://leetcode.com/contest/biweekly-contest-74/problems/divide-array-into-equal-pairs/

from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nCounter = Counter(nums)
        
        ok = True
        for key in nCounter:
            if nCounter[key]%2>0:
                ok = False
        return ok