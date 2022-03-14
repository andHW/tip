# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        for i in range(numRows):
            lastR = res[-1]
            newRow = [1] + [a+b for a, b in zip(lastR, lastR[1:])] + [1]
            res.append(newRow)
        return res[:numRows]
