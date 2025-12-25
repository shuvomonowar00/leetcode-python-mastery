'''
    547. Number of Provinces
    TC: O()
    SC: O()
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set([])
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                stack = [i]
                while stack:
                    top = stack.pop()
                    visited.add(top)
                    for j in range(len(isConnected)):
                        if j not in visited and isConnected[top][j] == 1:
                            stack.append(j)
                count += 1
        return count

            
