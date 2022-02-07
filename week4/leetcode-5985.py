# https://leetcode.com/contest/biweekly-contest-71/problems/partition-array-according-to-given-pivot/
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        m = []
        r = []

        for n in nums:
            if n == pivot:
                m += [n]
            elif n < pivot:
                l += [n]
            else:
                r += [n]

        return l+m+r


s = Solution()
print(s.pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10))
