"""
    735. Asteroid Collision
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for a in asteroids[1:]:
            while stack:
                if stack[-1] > 0 and a < 0 and stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] > 0 and a < 0 and stack[-1] > abs(a):
                    break
                elif stack[-1] > 0 and a < 0 and abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                else:
                    stack.append(a)
                    break
            else:
                stack.append(a)
        return stack

                    
                   
