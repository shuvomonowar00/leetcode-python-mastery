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
        def hasPathSumRecur(node: Optional[TreeNode], arr: List[int]):
            if not node:
                return
            arr.append(node.val)
            if not node.left and not node.right and sum(arr) ==  self.targetSum:
                self.dcsn = True
                return
            hasPathSumRecur(node.left, arr)
            hasPathSumRecur(node.right, arr)
            arr.pop()
        hasPathSumRecur(root, [])
        return self.dcsn
