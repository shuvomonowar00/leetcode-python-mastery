"""
    Equal Row and Column Pairs 2352
    Time Complexity - O(n^3)
    Space Complexity - O(n^2)
"""

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gl = len(grid)
        c = 0

        # Complete the dictionary portion
        for i in range(gl):
            tl = []
            for j in range(gl):
                tl.append(grid[j][i])
            for k in range(gl):
                if tl == grid[k]:
                    c += 1
        return c


if __name__ == "__main__":
    obj = Solution()
    obj.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
