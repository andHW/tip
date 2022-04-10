# https://practice.geeksforgeeks.org/contest/interview-series-45/problems
# Number of Subarrays of 0's
class Solution():
    def no_of_subarrays(self, n,nums):
        ans = 0
        runningSum = 0
        last0 = -1
        
        for i, c in enumerate(nums):
            if c == 1:
                last0 = -1
            else:
                ans += 1 
                if last0 <0:
                    last0 = i
                else:
                    ans += i-last0
        return ans
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends