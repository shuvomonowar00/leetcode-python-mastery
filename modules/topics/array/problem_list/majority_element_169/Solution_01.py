"""
    169. Majority Element
"""

from typing import List

class Solution_01:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        item = 0
        count = 0
        i = 0
        while i < len(nums):
            j = i
            c = 0
            while j < len(nums) and nums[j] == nums[i]:
                c += 1
                j += 1
            if c > count:
                item = nums[i]
                count = c
            i = j
        return item
            

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.majorityElement([2,2,1,1,1,2,2,3]))