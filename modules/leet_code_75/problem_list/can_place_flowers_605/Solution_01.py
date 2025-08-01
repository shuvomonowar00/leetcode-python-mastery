'''
   605. Can Place Flowers 
'''
from typing import List


class Solution_01:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        else:
            if len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    if n == 1:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                for i in range(1, len(flowerbed)-1):
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                    if n == 0:
                        print(flowerbed)
                        return True
                
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    n -= 1
                    if n == 0:
                        print(flowerbed)
                        return True

                if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
                    n -= 1
                    if n == 0:
                        print(flowerbed)
                        return True
            print(flowerbed)
            print(n)
            return False


if __name__ == '__main__':
  obj = Solution_01()
  print(obj.canPlaceFlowers(flowerbed = [0,0,0,0,1], n = 2))
                

                 

