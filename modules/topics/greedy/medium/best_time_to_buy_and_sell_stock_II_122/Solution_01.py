"""
    122. Best Time to Buy and Sell Stock II
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.profit = 0
        def max_profit(s, p):
            if p >= len(self.prices)-1:
                return

            if s is False:
                p += 1
                s = True
            else:
                if self.prices[p] < self.prices[p+1]:
                    self.profit += self.prices[p+1] - self.prices[p]
                    s = True
                    p += 1
                else:
                    s = False
                    
            max_profit(s, p)

        max_profit(False, -1)
        return self.profit


