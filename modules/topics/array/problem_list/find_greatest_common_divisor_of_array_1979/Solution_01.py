from typing import List


class Solution_01:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        while x > 0 and y > 0:
            if x > y:
                x = x%y
            else:
                y = y%x
            
        return max(x,y)


if __name__ == '__main__':
    obj = Solution_01()
    print(obj.findGCD([3,3]))
