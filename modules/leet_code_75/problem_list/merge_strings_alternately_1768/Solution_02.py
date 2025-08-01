'''
    This solution is based on more optimized way
'''
from typing import List


class Solution_02:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out_str: List[str] = []
        count: int = 0

        while count < int(min(len(word1), len(word2))):
            out_str.append(word1[count])
            out_str.append(word2[count])
            count += 1

        out_str.append(word1[count:])
        out_str.append(word2[count:])

        return "".join(out_str)
    

if __name__ == '__main__':
    word1, word2 = input(), input()
    obj = Solution_02()
    print(obj.mergeAlternately(word1, word2))