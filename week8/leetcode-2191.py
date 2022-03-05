class Solution:
    def getMappedNum(self, mapping: List[int], n) -> int:
        resS = [str(mapping[int(d)]) for d in str(n)]
        return int("".join(resS))

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ss = []
        for i, n in enumerate(nums):
            mapped = self.getMappedNum(mapping, n)
            ss.append((mapped, i, n))
        ss.sort()
        print(ss)

        res = [s[-1] for s in ss]

        return res
