'''
    151. Reverse Words in a String
'''
from typing import List


class Solution_01:
    #Solution 01
    # def reverseWords(self, s: str) -> str:
    #     nsl: List[str] = []
    #     ts: str = ""
    #     for i in range(len(s)):
    #         if s[i] == ' ':
    #             nsl.append(ts)
    #             ts = ""
    #         elif i == len(s)-1:
    #             ts += s[i]
    #             nsl.append(ts)
    #         else:
    #             ts += s[i] 
    #     nsl = [i for i in nsl if i != ""]
    #     nsl.reverse()
    #     return " ".join(nsl)

    # Solution 02 (More optimized way)
    def reverseWords(self, s: str) -> str:
        nsl: List[str] = s.split()
        nsl.reverse()
        return " ".join(nsl)


if __name__ == "__main__":
    obj = Solution_01()
    print(obj.reverseWords(" hello world "))       