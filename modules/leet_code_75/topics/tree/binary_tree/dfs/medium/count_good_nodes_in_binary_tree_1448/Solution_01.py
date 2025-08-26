"""
    1448. Count Good Nodes in Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c = 0
        def recur_func(root, pgnv):
            if not root:
                return
            elif pgnv <= root.val:
                self.c += 1
                pgnv = root.val
            recur_func(root.left, pgnv)
            recur_func(root.right, pgnv)
        recur_func(root, -10 ** 5)
        return self.c
            