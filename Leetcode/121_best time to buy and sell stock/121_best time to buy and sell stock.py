class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_num = float('inf')
        for price in prices:
            min_num = min(min_num, price)
            profit = max(profit, price - min_num)
        return profit