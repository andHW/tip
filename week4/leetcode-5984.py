# https://leetcode.com/contest/biweekly-contest-71/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution:
    def minimumSum(self, num: int) -> int:
        sum = 0
        ds = [ int(d) for d in str(num) ]
        ds.sort()
        sum = ds[0]*10+ds[1]*10+ds[2]+ds[3]
        return sum

s = Solution()
print(s.minimumSum(num=4009))