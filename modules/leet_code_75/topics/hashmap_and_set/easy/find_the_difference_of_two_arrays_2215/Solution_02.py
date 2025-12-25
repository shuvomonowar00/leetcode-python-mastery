"""
    2215. Find the Difference of Two Arrays
    Time Complexity -> O(n + m)
    Space Complexity -> O(n + m)
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums)-set(nums2)), list(set(nums2)-set(nums1))]
         