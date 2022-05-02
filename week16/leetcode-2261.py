class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        magic = [int(nums[0]%p==0)]
        
        for i in range(1, len(nums)):
            magic.append(magic[i-1]+int(nums[i]%p==0))
        
        magic = [0] + magic
        
        # print(magic)
        stupid = set()
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)+1):
                md = magic[j]-magic[i]
                # print(f"{nums[i:j]} md:{md}")
                if md > k:
                    break
                sa = tuple(nums[i:j])
                stupid.add(sa)
        # print(stupid)
        return len(stupid)