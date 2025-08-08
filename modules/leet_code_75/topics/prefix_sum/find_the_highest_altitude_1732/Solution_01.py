"""
    1732. Find the Highest Altitude
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_val = 0
        pref_sum = 0
        for i in range(len(gain)):
            pref_sum += gain[i]
            if pref_sum > max_val:
                max_val = pref_sum
        return max_val
                