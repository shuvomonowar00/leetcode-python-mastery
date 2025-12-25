'''
    1466. Reorder Routes to Make All Paths Lead to the City Zero
    TC: O()
    SC: O()
'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_lis = {}
        # Create adjacency list
        for i in range(len(connections)):
            if connections[i][0] in adj_lis:
                adj_lis[connections[i][0]].append(connections[i][1])
            else:
                adj_lis[connections[i][0]] = []
        
        c = 0
        visited = set([])
        for k in adj_lis:
            if k not in visited: 
                tc = 0
                stack = [k]
                while stack:
                    top = stack.pop()
                    visited.add(top)
                    for i in adj_lis[top]:
                        if i == 0:
                            tc = 0
                        if i not in visited:
                            tc += 1
                            stack.append(i)
            c += tc
        return c          
                        
