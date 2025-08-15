"""
    872. Leaf-Similar Trees
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collectingLeafNodes(node):
            if not node:
                return []
            elif not node.left and not node.right:
                return [node.val]
            return collectingLeafNodes(node.left)+collectingLeafNodes(node.right)
        return collectingLeafNodes(root1) == collectingLeafNodes(root2)
