"""
    735. Asteroid Collision
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        if len(asteroids) > 1:
            for i in asteroids[1:]:
                if stack[-1] is None:
                    stack.append(i)
                else:
                    while len(stack) > 0 and (abs(stack[-1]) != abs(i) and (stack[-1] > 0 and i < 0)):  
                        if abs(stack[-1]) < abs(i):
                            stack.pop()
                        else:
                            stack.append(i)
                            break
                    if len(stack) > 0 and stack[-1] == i or (abs(stack[-1]) == abs(i) and (stack[-1] > 0 and i < 0)):
                        stack.pop()
                    if len(stack) and stack[-1] != i and ((stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i < 0)):
                        stack.append(i)
        return stack
                
                    
                   
