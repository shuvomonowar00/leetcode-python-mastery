"""
    122. Best Time to Buy and Sell Stock II -> Using DP (Dynamic Programming)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.l = len(prices)
        self.prices = prices
        self.memo = {}
        def recMaxProf(stock, state):
            if state >= self.l:
                return 0
            elif (stock, state) in self.memo:
                return self.memo[(stock, state)]
            elif stock == 0:
                buy = -self.prices[state] + recMaxProf(1, state+1)
                skip = 0 + recMaxProf(0, state+1)
                profit = max(buy, skip)
                self.memo[(stock, state)] = profit
                return profit
            elif stock == 1:
                sell = self.prices[state] + recMaxProf(0, state+1)
                hold = 0 + recMaxProf(1, state+1)
                profit = max(sell, hold)
                self.memo[(stock, state)] = profit
                return profit
        return recMaxProf(0, 0)



