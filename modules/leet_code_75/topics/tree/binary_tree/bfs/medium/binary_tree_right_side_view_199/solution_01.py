"""
    199. Binary Tree Right Side View
    Time Complexity: O(N)
    Space Complexity: O(N)
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # q = []
        # if not root:
        #     return q
        # q.append(root)
        # fs = []
        # while q:
        #     len_q = len(q)
        #     ts = []
        #     for _ in range(len_q):
        #         if q[0].left:
        #             q.append(q[0].left)
        #         if q[0].right:
        #             q.append(q[0].right)
        #         p = q.pop(0)
        #         ts.append(p.val)
        #     fs.append(ts[len(ts)-1])
        # return fs

        # Using deque
        if not root:
            return []
        q = deque([root])
        fl = []
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
            fl.append(tl[-1])
        return fl
