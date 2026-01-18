'''
    Problem: 2300. Successful Pairs of Spells and Potions
    Time Complexity: O(mlogm + nlogm)
    Space Complexity: O(n)
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # TC->O(mlogm), SC->O(logm)
        fl = [] # SC->O(n)
        for s in spells: # TC->O(nlogm)
            low, high = 0, len(potions)-1
            fmid = 0
            while low <= high: # TC->O(logm), SC->O(1)
                mid = (low + high) // 2
                if potions[mid]*s < success:
                    low = mid+1
                    fmid = mid
                elif potions[mid]*s >= success:
                    high = mid-1
                    fmid = mid - 1
            fl.append(len(potions)-(fmid+1))
        return fl

