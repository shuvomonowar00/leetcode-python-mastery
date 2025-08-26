# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.dcsn = False
        def hasPathSumRecur(node: Optional[TreeNode], prevSum: int):
            if not node:
                return
            prevSum = prevSum + node.val
            if not node.left and not node.right and prevSum ==  self.targetSum:
                self.dcsn = True
                return
            hasPathSumRecur(node.left, prevSum)
            hasPathSumRecur(node.right, prevSum)
        hasPathSumRecur(root, 0)
        return self.dcsn
