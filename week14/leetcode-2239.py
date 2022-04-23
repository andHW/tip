class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        nums.sort()
        for n in nums:
            if abs(n) <= abs(ans):
                ans = n
        return ans