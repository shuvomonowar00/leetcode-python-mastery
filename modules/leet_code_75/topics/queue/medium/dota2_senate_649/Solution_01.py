"""
    649. Dota2 Senate
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ls = list(senate)
        cr = ls.count("R")
        cd = ls.count("D")
        i = 0
        j = 1

        while j < len(ls):
            if ls[i] != ls[j]:
                if ls[j] == "R":
                    cr -= 1
                else:
                    cd -= 1
                    
                ls.pop(j)
                ls.append(ls[i])
                ls.pop(i)
                j = 1

                if cr == 0 or cd == 0:
                    break
                continue
            j += 1

        if cr == 0:
            return "Dire"
        return "Radiant"
