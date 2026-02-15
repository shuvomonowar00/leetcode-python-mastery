'''
    Problem: 
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        length = len(nums)

        # Sort the list
        while start < length:
            j = nums[start]
            if nums[start] < length and nums[start] != nums[nums[start]]:
                nums[start], nums[j] = nums[j], nums[start]
            else:
                start += 1
            
        # Find the missing number
        for i in range(length):
            if i != nums[i]:
                return i
        
        return length