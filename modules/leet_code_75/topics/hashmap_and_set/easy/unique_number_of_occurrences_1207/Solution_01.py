"""
1207. Unique Number of Occurrences
"""

from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ad = defaultdict(int)
        for a in arr:
            ad[a] += 1
        
        sd = set(ad.values())
        if len(ad) == len(sd):
            return True
        return False
