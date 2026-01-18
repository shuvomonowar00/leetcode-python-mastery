'''
    Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
    Time Complexity: O(n)
    Space Complexity: O(1)
    Auxiliary Space: 0(1)
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vow = 0
        curr_vow = 0
        last_idx = 0

        # Count first window vowels
        for i in range(k):
            if s[i] in vowels:
                curr_vow += 1
        max_vow = curr_vow

        # Operate sliding window to the others
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_vow += 1
            if s[last_idx] in vowels:
                curr_vow -= 1
            max_vow = max(curr_vow, max_vow)
            last_idx += 1
        
        return max_vow



