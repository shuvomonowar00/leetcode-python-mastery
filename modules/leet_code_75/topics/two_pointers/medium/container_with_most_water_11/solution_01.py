'''
    Problem: 11. Container With Most Water
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = 0

        while l < r:
            if height[l] < height[r]:
                area = max(area, (r-l)*height[l])
                l += 1
            else:
                area = max(area, (r-l)*height[r])
                r -= 1
        
        return area
