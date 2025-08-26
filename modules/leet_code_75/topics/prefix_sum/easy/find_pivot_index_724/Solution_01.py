"""
    724. Find Pivot Index
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        while i < l:
            if i == 0 and i == l-1:
                return i
            elif i == 0 and i < l-1:
                if sum(nums[i+1:]) == 0:
                    return i
            elif i == l-1 and l-1 != 0:
                if sum(nums[:i]) == 0:
                    return i
            elif sum(nums[:i]) == sum(nums[i+1:]):
                return i
            i += 1
        return -1