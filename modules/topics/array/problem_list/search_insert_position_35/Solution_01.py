from typing import  List


class Solution_01:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # If the target value is existed in the list
        while low <= high:
            mid = low + (high - low) // 2 # Find the mid-index
            if nums[mid] != target:
                if nums[mid] < target:
                    low = mid
                else:
                    high = mid
            else:
                return mid
        # If the target value is not existed in the list
        return low


s1 = Solution_01()
print(s1.searchInsert([2,7,11,15], 9))

