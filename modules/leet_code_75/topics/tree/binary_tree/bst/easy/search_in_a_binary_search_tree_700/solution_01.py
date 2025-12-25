"""
    700. Search in a Binary Search Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == val:
            return root
        else:
            res = None
            if root.val > val:
                res = self.searchBST(root.left, val)
            else:
                res = self.searchBST(root.right, val)
            return res
            

