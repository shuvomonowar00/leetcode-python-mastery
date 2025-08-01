'''
    283. Move Zeroes
'''
from typing import List


class Solution_01:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                k = i
                while nums[k] == 0:
                    k += 1
                nums[j] = nums[k]
                nums[k] = 0
                j = -1
        print(nums)


if __name__ == "__main__":
    obj = Solution_01()
    obj.moveZeroes([0, 1, 0, 3, 12])


        