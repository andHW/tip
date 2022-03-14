# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastR = [1]
        for i in range(rowIndex):
            newRow = [1] + [a+b for a, b in zip(lastR, lastR[1:])] + [1]
            lastR = newRow
        return lastR
