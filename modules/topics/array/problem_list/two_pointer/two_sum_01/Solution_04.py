from typing import List


class Solution_03:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [nums_dict[target-nums[i]], i]
            nums_dict[nums[i]] = i



if __name__ == '__main__':
    obj = Solution_03()
    print(obj.twoSum([2222222, 2222222], 4444444))
    # print(obj.twoSum([3, 2, 4], 6))









