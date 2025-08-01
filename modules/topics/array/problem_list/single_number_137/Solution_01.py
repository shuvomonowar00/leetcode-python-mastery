from typing import List


class Solution_01:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i != len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 3
                continue
            return nums[i]
        return nums[-1]


obj = Solution_01()
print(obj.singleNumber([2,2,3,2]))
        