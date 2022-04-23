class Solution:
    def digitSum(self, s: str, k: int) -> str:
        nums = [int(c) for c in s]
        while len(nums) > k:
            newNums = [0]* (len(nums)//k + int(len(nums)%k>0))
            c = 0
            ni = 0
            for n in nums:
                newNums[ni] += n
                c+=1
                if c==k:
                    ni+=1
                    c = 0
            nums = [int(c) for c in "".join([str(n) for n in newNums])]
            
        return "".join([str(n) for n in nums])
                    
                
                