"""
    242. Valid Anagram - solved using hashmap
"""

class Solution_01:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] = s_map[s[i]] + 1
            
            if t[i] not in t_map:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] = t_map[t[i]] + 1
        return s_map == t_map
            

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.isAnagram(s = "anagram", t = "nagaran"))