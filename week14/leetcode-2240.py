class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # cost = x*cost1 + y*cost2
        # cost <= total
        ways = 0
        for i in range(total//cost1+1):
            moneyLeft = total - cost1*i
            ways+= moneyLeft//cost2+1
        return ways