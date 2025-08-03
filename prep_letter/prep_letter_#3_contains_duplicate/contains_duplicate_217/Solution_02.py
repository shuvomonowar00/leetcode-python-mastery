"""
    217. Contains Duplicate
"""

from typing import List


class Solution_01:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.containsDuplicate([1,2,3,1]))