# https://leetcode.com/contest/weekly-contest-279/problems/sort-even-and-odd-indices-independently/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []

        isOdd = False
        for n in nums:
            if isOdd:
                odds += [n]
            else:
                evens += [n]
            isOdd = not isOdd
        evens.sort()
        odds.sort(reverse=True)

        res = []

        for e, o in zip(evens, odds):
            res += [e, o]

        if len(evens) > len(odds):
            res += [evens[-1]]

        if len(evens) < len(odds):
            res += [odds[-1]]

        return res
