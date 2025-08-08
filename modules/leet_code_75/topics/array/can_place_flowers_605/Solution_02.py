'''
   605. Can Place Flowers 
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        c = 0
        s = 0
        if l == 1 and and flowerbed[0] == 0:
            c += 1
        else:
            for i in range(len(flowerbed)-1):
                if s == flowerbed[i] == flowerbed[i+1] == 0:
                    c += 1
                    flowerbed[i] = 1
                s = flowerbed[i]
                if c >= n:
                    break
            if c < n:
                if flowerbed[l-1] = flowerbed[l-2] = 0:
                    c += 1
        if c >= n:
            return True
        return False

        
if __name__ == '__main__':
  obj = Solution_01()
  print(obj.canPlaceFlowers(flowerbed = [0,0,0,0,1], n = 2))
                

                 

