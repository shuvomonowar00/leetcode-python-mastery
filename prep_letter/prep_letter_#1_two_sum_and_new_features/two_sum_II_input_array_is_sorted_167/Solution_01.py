'''
    167. Two Sum II - Input Array Is Sorted
'''

from typing import List


class Solution_01:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] < target:
                l += 1
            else:
                r -= 1

        return [l+1, r+1]


if __name__ == '__main__':
    obj = Solution_01()
    print(obj.twoSum([2,7,11,15], 9))
