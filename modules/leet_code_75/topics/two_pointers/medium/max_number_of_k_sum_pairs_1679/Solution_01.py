"""
    1679. Max Number of K-Sum Pairs
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0

        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] = nums_dict[num] + 1
            else:
                nums_dict[num] = 1

        for num in nums:
            next_num = k-num
            if num == next_num and nums_dict[num] > 1:
                nums_dict[num] = nums_dict[num] - 2
                c += 1
            elif num != next_num and nums_dict[num] > 0 and next_num in nums_dict and nums_dict[next_num] > 0:
                nums_dict[num] = nums_dict[num] - 1
                nums_dict[next_num] = nums_dict[next_num] - 1
                c += 1
        return c

