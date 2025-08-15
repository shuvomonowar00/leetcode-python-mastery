"""
    933. Number of Recent Calls
"""

from collections import deque

class RecentCounter:

    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        self.d.append(t)

        la = t-3000
        fp = self.d[0]
        while fp < la:
            self.d.popleft()
            fp = self.d[0]
        return len(self.d)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)