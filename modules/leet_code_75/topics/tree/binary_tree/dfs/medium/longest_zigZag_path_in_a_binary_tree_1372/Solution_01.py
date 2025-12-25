"""
    1372. Longest ZigZag Path in a Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.tc = 0
        self.d = -1 # 1 means left and 0 means right
        def lzz(node, d):
            if node and d == 1:
                self.tc += 1
                lzz(node.right, 0)
                self.tc = 0
                lzz(node.left, 1)
            elif node and d == 0:
                self.tc += 1
                lzz(node.left, 1)
                self.tc = 0
                lzz(node.right, 0)
            elif not node:
                if self.tc > self.count:
                    self.count = self.tc
                self.tc = 0
                return
            else:
                lzz(node.left, 1)
                lzz(node.right, 0)
        lzz(root, self.d)
        return self.count

            



