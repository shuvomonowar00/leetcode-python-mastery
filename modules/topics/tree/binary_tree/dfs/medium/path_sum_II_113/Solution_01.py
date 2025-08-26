"""
    113. Path Sum II
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.sum_arr = []
        self.targetSum = targetSum
        def pathSumRecur(node: Optional[TreeNode], sum_arr: List[int]):
            if not node:
                return
            sum_arr.append(node.val)
            if not node.left and not node.right and sum(sum_arr) == self.targetSum:
                self.sum_arr.append(sum_arr.copy())
            pathSumRecur(node.left, sum_arr)
            pathSumRecur(node.right, sum_arr)
            sum_arr.pop() # Backtracking
        pathSumRecur(root, [])
        return self.sum_arr