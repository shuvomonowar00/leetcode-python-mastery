'''
    841. Keys and Rooms
    Time Complexity: O(N^2)
    Space Complexity: O(N)
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([])
        def cvar(key):
            if key in visited:
                return
            visited.add(key)
            for i in rooms[key]:
                cvar(i)
        cvar(0)
        return len(visited) == len(rooms)
