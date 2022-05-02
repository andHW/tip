# https://leetcode.com/contest/biweekly-contest-77/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        ans = 0
        leftSum = nums[0]
        leftAvg = leftSum
        rightSum = sum(nums[1:])
        rightAvg = rightSum // (len(nums)-1)

        minAvg = abs(leftAvg - rightAvg)

        for i in range(1, len(nums)):
            leftSum += nums[i]
            rightSum -= nums[i]
            leftAvg = leftSum // (i+1)
            rightAvg = rightSum // max(1, len(nums)-i-1)
            avg = abs(leftAvg-rightAvg)
            
            if avg < minAvg:
                minAvg = avg
                ans = i
            

        return ans