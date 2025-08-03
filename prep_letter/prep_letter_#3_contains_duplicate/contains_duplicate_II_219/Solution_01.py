"""
    219. Contains Duplicate II
"""

from typing import List


class Solution_01:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}
        for i in range(len(nums)):
            # if nums[i] not in nums_map:
            #     nums_map[nums[i]] = i+1
            # else:
            #     if (i+1)-nums_map[nums[i]] <= k:
            #         return True
            #     nums_map[nums[i]] = i+1
            if nums[i] in nums_map and (i+1)-nums_map[nums[i]] <= k:
                return True
            nums_map[nums[i]] = i+1
        return False
                    

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))