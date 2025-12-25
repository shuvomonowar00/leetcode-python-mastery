"""
    1137. N-th Tribonacci Number
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tbn(n) -> int:
            if n in memo:
                return memo[n]
            elif n == 2:
                memo[n] = 1
                return 1
            elif n == 0 or n == 1:
                memo[n] = n
                return n
            num = tbn(n-1) + tbn(n-2) + tbn(n-3)
            memo[n] = num
            return num
        return tbn(n)
    

