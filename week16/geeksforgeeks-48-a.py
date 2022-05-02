# https://practice.geeksforgeeks.org/contest/interview-series-48/problems/

class Solution():
    def minimumChanges(self, s):
        ans = 0
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
               ans +=1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().minimumChanges(s))
# } Driver Code Ends