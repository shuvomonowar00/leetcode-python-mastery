from typing import List


class Solution_01:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j]-prices[i] > max_prof:
                max_prof = prices[j]-prices[i]
            if prices[j] < prices[i]:
                i = j
            j += 1
        return max_prof


            


if __name__ == "__main__":
    obj = Solution_01()
    print(obj.maxProfit([2,4,1]))