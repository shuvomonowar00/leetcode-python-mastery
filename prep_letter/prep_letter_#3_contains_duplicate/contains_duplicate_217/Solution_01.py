"""
    217. Contains Duplicate
"""

from typing import List


class Solution_01:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set: set[int] = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.containsDuplicate([1,2,3,1]))