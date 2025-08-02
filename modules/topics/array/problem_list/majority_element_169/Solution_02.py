"""
    169. Majority Element
"""

from typing import List


class Solution_01:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        item = nums[len(nums)-1]
        count = 1
        tcount = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                tcount += 1
                if i+1 == len(nums)-1:
                    if tcount > count:
                        item = nums[i]
                        count = tcount
            else:
                if tcount > count:
                    item = nums[i]
                    count = tcount
                tcount = 1
            
        return item
            

if __name__ == "__main__":
    obj = Solution_01()
    print(obj.majorityElement([2,2,1,1,1,2,2,3]))