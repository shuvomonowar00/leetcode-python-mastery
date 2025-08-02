"""
    169. Majority Elements solved with Boyer Moor's Voting Algorithm
"""

from typing import List


class Solution_04:
    def majorityElement(self, nums: List[int]) -> int:
        top = -1
        count = 0
        for num in nums:
            if count == 0:
                top = num
                count += 1
            elif num == top:
                count += 1
            else:
                count -= 1
        return top
            

if __name__ == "__main__":
    obj = Solution_04()
    print(obj.majorityElement([2,2,1,1,1,1,1,2,2]))