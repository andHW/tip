class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        magic=[(nums[0],1)]
        
        for n in nums[1:]:
            if n!=magic[-1][0]:
                magic.append((n,1))
            else:
                magic[-1] = (n, magic[-1][1]+1)
        
        print(magic)
        for i in range(1,len(magic)-1):
            l,mid,r = map(lambda x: x[0],magic[i-1:i+2])
            print("---------")
            print(l,mid,r)
            print("---------")
            if mid <l and mid < r:
                ans+=1
            if mid>l and mid >r:
                ans+=1
        return ans