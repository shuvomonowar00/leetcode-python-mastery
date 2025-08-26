"""
    1071. Greatest Common Divisor of Strings
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        if str1+str2 != str2+str1:
            return ""
        def gs(a, b):
            if min(a, b) == 0:
                return max(a, b)
            return gs(min(a, b), max(a, b) % min(a, b))
        return str1[:gs(l1, l2)]
