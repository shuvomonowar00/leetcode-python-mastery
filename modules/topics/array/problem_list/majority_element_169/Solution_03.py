"""
    169. Majority Element
"""

from typing import List


"""
    169. Majority Element
"""

from typing import List

class Solution_01:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] = nums_map[num] + 1
        return max(nums_map, key=nums_map.get)
            

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.majorityElement([2,2,1,1,1,1,1,2,2,]))