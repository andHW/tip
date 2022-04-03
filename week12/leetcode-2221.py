# https://leetcode.com/contest/biweekly-contest-75/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        nLen = len(nums)
        ns = nums
        newNs  = []
        for i in range(nLen-1):
            newNs  = []
            for a,b in zip( ns, ns[1:] ):
                newNs.append((a+b)%10)
            # print(newNs)
            ns = newNs
        
        if newNs:
            return (sum(newNs))
        return (sum(nums))