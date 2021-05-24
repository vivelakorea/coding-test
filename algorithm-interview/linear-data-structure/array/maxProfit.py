from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = sys.maxsize
        profit = 0
        for price in prices:
            buying_price = min(buying_price, price)
            profit = max(profit, price - buying_price)
        return profit

s = Solution()
print(s.maxProfit([7,6,4,3,1]))

