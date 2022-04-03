# https://practice.geeksforgeeks.org/contest/interview-series-intuit-1134/problems/

class Solution():
    def countZero(self, n, k ,tasks):
        res = []
        
        operatedR = set()
        operatedC = set()
        rc = cc = 0
        
        for task in tasks:
            r,c = task
            
            if r not in operatedR:
                operatedR.add(r)
                rc+=1
            
            if c not in operatedC:
                operatedC.add(c)
                cc+=1
            
            # print("R:"+str(rc)+"    C:"+str(cc))
            numOf0 = n*n - (rc*n + (n-rc)*cc)
            
            res.append(numOf0)
             
        return res
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Endsclass Solution():
    def countZero(self, n, k ,tasks):
        res = []
        
        operatedR = set()
        operatedC = set()
        rc = cc = 0
        
        for task in tasks:
            r,c = task
            
            if r not in operatedR:
                operatedR.add(r)
                rc+=1
            
            if c not in operatedC:
                operatedC.add(c)
                cc+=1
            
            # print("R:"+str(rc)+"    C:"+str(cc))
            numOf0 = n*n - (rc*n + (n-rc)*cc)
            
            res.append(numOf0)
             
        return res
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends