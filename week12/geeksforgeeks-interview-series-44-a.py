# https://practice.geeksforgeeks.org/contest/interview-series-44/problems

class Solution:
    def inSequence(self, A, B, C):
        if C ==0:
            return int(A==B)
        res = (B-A)/C == (B-A)//C and (B-A)//C >= 0
        return int(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]
        
        ob = Solution();
        print(ob.inSequence(A, B, C))
# } Driver Code Ends