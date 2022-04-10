# https://leetcode.com/contest/weekly-contest-288/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        snum = str(num)
        nums = list(map(int,list(snum)))
        
        ePlaces = [i for i, num in enumerate(nums) if num%2<1]
        
        oNums = [num for num in nums if num%2>0]
        eNums = [num for num in nums if num%2<1]
        oNums.sort(reverse=True)
        eNums.sort(reverse=True)
        
        dumb = [-1]*len(nums)
        
        iii = 0
        for e in ePlaces:
            dumb[e] = eNums[iii]
            iii+=1
        
        iii=0
        for i in range(len(dumb)):
            if dumb[i]==-1:
                dumb[i] = oNums[iii]
                iii+=1
                
        
        return int( "".join(map(str,dumb) ))