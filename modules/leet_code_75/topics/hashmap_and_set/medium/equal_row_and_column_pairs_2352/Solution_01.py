"""
    2352. Equal Row and Column Pairs
    Time Complexity - O(n^3)
    Space Complexity - O(n^2)
"""

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gl = len(grid)
        gs = {}

        # Complete the dictionary portion
        for i in range(gl):
            tl = []
            for j in range(gl):
                tl.append(grid[j][i])
            gs[i] = tl
        
        # Debug purposes
        print(gs)

        # Complete the mapping portion
        c = 0
        for i in range(gl):
            for j in range(gl):
                if grid[i] == gs[j]:
                    c += 1
        # print(c)
        return c


if __name__ == "__main__":
    obj = Solution()
    obj.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
