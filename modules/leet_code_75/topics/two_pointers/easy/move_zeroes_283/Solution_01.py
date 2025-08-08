"""
    283. Move Zeroes
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zi = -1
        # for nzi in range(len(nums)-1):
        #     if nums[nzi] == 0:
        #         zi = nzi
        #         while nzi < len(nums) and nums[nzi] == 0:
        #             nzi += 1
        #         if nzi < len(nums):
        #             tmp = nums[zi]
        #             nums[zi] = nums[nzi]
        #             nums[nzi] = tmp
        #         nzi = zi + 1

        i = 0
        j = 0
        while i < len(nums):
            j += 1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                if j == len(nums):
                    break
                continue
            if j == len(nums):
                break
            i += 1
            

                

