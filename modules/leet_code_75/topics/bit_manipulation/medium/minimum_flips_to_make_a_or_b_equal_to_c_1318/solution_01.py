'''
    Problem: 1318. Minimum Flips to Make a OR b Equal to c 
    Time Complexity: O(O(log(max(a, b, c))))
    Space Complexity: O(1)
    Auxiliary Space: 
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mf = 0

        while a>0 or b>0 or c>0:
            abit = a&1
            bbit = b&1
            cbit = c&1

            if cbit == 0:
                mf += abit+bbit
            else:
                if abit == 0 and bbit == 0:
                    mf += 1
            
            a >>= 1
            b >>= 1
            c >>= 1

        return mf