# https://leetcode.com/contest/weekly-contest-286/problems/minimum-deletions-to-make-array-beautiful/

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        a = 0
        p = nums[0]
        lc = nums[0]
        i = 1
        while i < len(nums):
            if (i+a) % 2 == 0:
                lc = nums[i]
            else:
                if nums[i] == lc:
                    a += 1
                else:
                    lc = ""
            i += 1
        return a+(len(nums)-a) % 2
