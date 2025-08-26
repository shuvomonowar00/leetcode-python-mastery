"""
    123. Best Time to Buy and Sell Stock III -> Using DP (Dynamic Programming)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.l = len(prices)
        self.prices = prices
        self.memo = {}
        def recMaxProf(stock, state, k):
            if state >= self.l or k == 0:
                return 0
            elif (stock, state, k) in self.memo:
                return self.memo[(stock, state, k)]
            elif stock == 0:
                buy = -self.prices[state] + recMaxProf(1, state+1, k)
                skip = 0 + recMaxProf(0, state+1, k)
                profit = max(buy, skip)
                self.memo[(stock, state, k)] = profit
                return profit
            elif stock == 1:
                sell = self.prices[state] + recMaxProf(0, state+1, k-1)
                hold = 0 + recMaxProf(1, state+1, k)
                profit = max(sell, hold)
                self.memo[(stock, state, k)] = profit
                return profit
        return recMaxProf(0, 0, 2)



