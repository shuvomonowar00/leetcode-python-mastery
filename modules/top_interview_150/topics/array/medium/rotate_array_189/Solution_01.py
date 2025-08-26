"""
    189. Rotate Array
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution - 01
        # while k > 0:
        #     nums.insert(0, nums[len(nums)-1])
        #     nums.pop()
        #     k -= 1

        # Solution - 02
        k = k % len(nums)
        if k != 0:
            nums[:0] = nums[-k:]
            nums[-k:] = []
        