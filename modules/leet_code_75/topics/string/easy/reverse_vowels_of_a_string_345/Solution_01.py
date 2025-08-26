"""
    345. Reverse Vowels of a String
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        self.sd = {"a": "a", "A": "A", "e": "e", "E": "E", "i": "i", "I": "I", "o": "o", "O": "O", "u": "u", "U": "U"}
        self.sl = list(s)
        def rrv(l, r):
            if l >= r:
                return
            else:
                if self.sl[l] not in self.sd and self.sl[r] not in self.sd:
                    l += 1
                    r -= 1
                elif self.sl[l] not in self.sd:
                    l += 1    
                elif self.sl[r] not in self.sd:
                    r -= 1
                else:
                    self.sl[l], self.sl[r] = self.sl[r], self.sl[l]
                    l += 1
                    r -= 1
            rrv(l, r)
        rrv(0, len(self.sl)-1)
        return "".join(self.sl)