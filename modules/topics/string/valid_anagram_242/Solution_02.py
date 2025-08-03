"""
    242. Valid Anagram - solved using sorting
"""

class Solution_01:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(s)
        t_list = sorted(t)
        return s_list == t_list

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.isAnagram(s = "anagram", t = "nagaram"))