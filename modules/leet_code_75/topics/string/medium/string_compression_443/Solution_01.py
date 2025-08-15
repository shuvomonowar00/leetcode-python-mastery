"""
    443. String Compression
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            j = i+1
            c = 1
            while j < len(chars):
                if chars[i] == chars[j]:
                    chars.pop(j)
                    c += 1
                else:
                    if c > 1:
                        cs = str(c)
                        k = 0
                        while k < len(cs):
                            chars.insert(i+1, cs[k])
                            i += 1
                            k += 1
                        c = 1
                    break
            if c > 1:
                cs = str(c)
                k = 0
                while k < len(cs):
                    chars.insert(i+1, cs[k])
                    i += 1
                    k += 1
                c = 1
            i += 1
            
        return len(chars)


                
