from typing import List


class Solution_03:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]

        for i in range(len(nums)):
            comprehension = target - nums[i]
            if comprehension in nums_dict:
                if i != nums_dict[comprehension][0]:
                    return [i, nums_dict[comprehension][0]]
                elif len(nums_dict[comprehension]) > 1:
                    return [i, nums_dict[comprehension][1]]




obj = Solution_03()
# print(obj.twoSum([2222222, 2222222], 4444444))
print(obj.twoSum([3, 2, 4], 6))









