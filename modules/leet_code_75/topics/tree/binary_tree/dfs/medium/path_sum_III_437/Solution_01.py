"""
    437. Path Sum III
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.arr = []
        self.targetSum = targetSum
        self.count = 0
        def recPathSum(node):
            if not node:
                return
            self.arr.append(node.val) # It measures the space complexity
            recPathSum(node.left)
            recPathSum(node.right)
            for i in range(len(self.arr)):
                if sum(self.arr[i:]) == targetSum:
                    self.count += 1
            self.arr.pop() # Backtracking
        recPathSum(root)
        return self.count

