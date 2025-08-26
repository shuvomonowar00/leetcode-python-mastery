"""
    345. Reverse Vowels of a String
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = set("AEIOUaeiou")
        sl = list(s)
        def rrv(l, r):
            if l >= r:
                return
            if sl[l] not in ss and sl[r] not in ss:
                l += 1
                r -= 1
            elif sl[l] not in ss:
                l += 1    
            elif sl[r] not in ss:
                r -= 1
            else:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
            rrv(l, r)
        rrv(0, len(sl)-1)
        return "".join(sl)