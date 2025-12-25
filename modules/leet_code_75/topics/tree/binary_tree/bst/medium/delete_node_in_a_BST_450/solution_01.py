"""
    450. Delete Node in a BST
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                sr = root.right
                parent = root
                while sr.left:
                    parent = sr
                    sr = sr.left
                root.val = sr.val
                if parent.right == sr:
                    parent.right = sr.right
                else:    
                    parent.left = sr.right
                return root
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
        return root
                    




