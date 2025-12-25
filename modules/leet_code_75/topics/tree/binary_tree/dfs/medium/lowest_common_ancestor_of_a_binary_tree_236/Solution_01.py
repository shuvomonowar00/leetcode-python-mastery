"""
    236. Lowest Common Ancestor of a Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        def lca(node):
            if not node or node == self.p or node == self.q or node.left == self.p and node.right == self.q or node.left == self.q and node.right == self.p:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            return left if left else right
        return lca(root)
            