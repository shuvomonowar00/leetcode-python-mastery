'''
   605. Can Place Flowers 
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        c = 0

        if l == 1 and flowerbed[0] == 0:
            c += 1
        elif l == 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            c += 1
        elif l == 3 and flowerbed[0] == 0 and flowerbed[0] == flowerbed[1] == flowerbed[2]:
            c += 2
        else:
            for i in range(l-2):
                if i == 0 and flowerbed[i] == flowerbed[i+1]:
                    flowerbed[i] = 1
                    c += 1
                elif i == l-3 and flowerbed[i] != 0 and flowerbed[i+1] == flowerbed[i+2] == 0:
                    c += 1
                elif flowerbed[i] == 0 and flowerbed[i] == flowerbed[i+1] == flowerbed[i+2]:
                    flowerbed[i+1] = 1
                    c += 1
        
        if n <= c:
            return True
        else:
            return False


if __name__ == '__main__':
  obj = Solution_01()
  print(obj.canPlaceFlowers(flowerbed = [0,0,0,0,1], n = 2))
                

                 

