# https://practice.geeksforgeeks.org/contest/interview-series-46/problems/#

#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        bs = [int(c.isupper()) for c in S]
        
        ones = 0
        zeros = 0
        for b in bs:
            if b==1:
                ones+=1
            else:
                zeros+=1
        
        magic = dict()
        tSum = 0
        for b in bs:
            if b==0:
                tSum-=1
            else:
                tSum+=1
            if tSum in magic:
                magic[tSum] += 1
            else:
                magic[tSum] = 1
        
        ans = 0
        for m in magic:
            if magic[m]>=2:
                ans += magic[m]*(magic[m]-1)//2
        if 0 in magic:
            ans+=magic[0]
        return ans
            
            

#{ 
#Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

#} Driver Code Ends