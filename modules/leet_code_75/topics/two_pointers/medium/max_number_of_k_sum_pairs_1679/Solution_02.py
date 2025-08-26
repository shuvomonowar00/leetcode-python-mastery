"""
    1679. Max Number of K-Sum Pairs
"""

from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nd = defaultdict(int)
        c = 0
        for num in nums:
            complement = k - num
            if nd[complement] > 0:
                nd[complement] -= 1
                c += 1
            else:
                nd[num] += 1
        return c

