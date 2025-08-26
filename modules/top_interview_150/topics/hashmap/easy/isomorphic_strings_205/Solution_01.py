"""
    205. Isomorphic Strings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        id = {}
        for i in range(len(s)):
            if s[i] in id:
                if t[i] != id[s[i]]:
                    return False
            else:
                if t[i] in id.values():
                    return False
                else:
                    id[s[i]] = t[i]
        return True
