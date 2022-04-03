
from collections import defaultdict

class Solution():
    def lexicographicallyLargest(self, a, n):
        i = 0
        while i<n-1:
            swap = -1
            aiIsOdd = a[i]%2>0
            largest = a[i]
            j=i+1
            ajIsOdd = a[j]%2>0
            if aiIsOdd and ajIsOdd or (not aiIsOdd and not ajIsOdd):
                if a[j] > largest:
                    swap = j
                    largest = a[j]
            
            if swap>-1:
                a[i],a[swap] = a[swap],a[i]
                if i>0:
                    i-=1
                    continue
            i+=1
        
        return a
        
        #your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
