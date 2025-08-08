'''
    2390. Removing Stars From a String
'''
from typing import List


class Solution_01:
    def removeStars(self, s: str) -> str:
        ss = []
        for ch in s:
            if ch == '*':
                ss.pop()
            else:
                ss.append(ch)
        return "".join(ss)


if __name__ == "__main__":
    obj = Solution_01()
    print(obj.removeStars("leet**cod*e"))