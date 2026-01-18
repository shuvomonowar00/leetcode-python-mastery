'''
    Problem: 374. Guess Number Higher or Lower
    Time Complexity: O(n)
    Space Complexity: O(1)
    Auxiliary Space: O(1)
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zc, la = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zc += 1
            
            while zc > 1:
                if nums[l] == 0:
                    zc -= 1
                l += 1
            
            la = max(la, r-l)
        
        return la
            


