class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        magic = [ set(l) for l in nums ]
        res = []
        for num in magic[0]:
            bad = False
            for i in range(1,len(magic)):
                if num not in magic[i]:
                    bad = True
                    break
            if bad:
                continue
            res.append(num)
        res = list(res)
        res.sort()
        return res