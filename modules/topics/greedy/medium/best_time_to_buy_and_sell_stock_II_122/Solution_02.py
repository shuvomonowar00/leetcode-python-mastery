"""
    122. Best Time to Buy and Sell Stock II
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = False
        sp = 0
        p = 0
        for i in range(len(prices)):
            if not s:
                s = True
                sp = prices[i]
            else:
                if sp < prices[i]:
                    p += prices[i]-sp
                    sp = prices[i]
                else:
                    sp = prices[i]
        return p




