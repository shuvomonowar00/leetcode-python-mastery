"""
    2215. Find the Difference of Two Arrays
    Time Complexity -> O(n + m)
    Space Complexity -> O(n + m)
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums_1 = set(nums1 + nums2)
        set_nums_2 = set(nums1 + nums2)
        for i in range(len(nums2)): # This is n
            if nums2[i] in set_nums_1:
                set_nums_1.remove(nums2[i])
        for i in range(len(nums1)): # THis is m
            if nums1[i] in set_nums_2:
                set_nums_2.remove(nums1[i])
        return [list(set_nums_1), list(set_nums_2)]
         