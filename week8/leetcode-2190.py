class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        weird = defaultdict(int)
        last = nums[0]
        for num in nums[1:]:
            if last == key:
                weird[num] += 1
            last = num

        return max(weird, key=weird.get)
