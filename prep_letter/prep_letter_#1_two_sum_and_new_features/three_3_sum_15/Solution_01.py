'''
    15. 3Sum
'''
from typing import List


class Solution_01:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fnl_lst: List[int] = []

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right] == 0:
                    fnl_lst.append([nums[i], nums[left], nums[right]])
                    left 
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        
        return fnl_lst


if __name__ == '__main__':
    obj = Solution_01()
    print(obj.threeSum([-1,0,1,2,-1,-4]))
        