# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float(inf)
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit
