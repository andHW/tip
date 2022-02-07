# https://leetcode.com/contest/biweekly-contest-71/problems/partition-array-according-to-given-pivot/
from typing import List


class Solution:
    def calCost(self, startAt: int, moveCost: int, pushCost: int, seq: List[int]) -> int:
        res = 0
        current = startAt
        for s in seq:
            if s != current:
                res += moveCost
            res += pushCost
            current = s
        return res

    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        ways = []
        for i in range(0, 10000):
            mmss = f'{i:04}'
            if int(mmss[:2])*60+int(mmss[2:]) == targetSeconds:
                way = [int(d) for d in mmss.lstrip('0')]
                ways += [way]
        print(ways)

        costs = [self.calCost(startAt, moveCost, pushCost, w) for w in ways]
        res = min(costs)

        return res


s = Solution()
print(s.minCostSetTime(startAt=0,
                       moveCost=1,
                       pushCost=2,
                       targetSeconds=76))
