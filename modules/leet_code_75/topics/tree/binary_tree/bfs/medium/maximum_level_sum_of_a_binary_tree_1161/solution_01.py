"""
    1161. Maximum Level Sum of a Binary Tree
    Time Complexity: O(N)
    Space Complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_val = root.val
        sl = 1
        tsl = 0
        while q:
            lq = len(q)
            tl = []
            for _ in range(lq):
                p = q.popleft()
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                tl.append(p.val)
            tsl += 1
            if max_val < sum(tl):
                max_val = sum(tl)
                sl = tsl
        return sl
