from typing import List


class Solution_01:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_list = len(nums)
        indx_list = []
        brk_loop = False
        for i in range(len_list-1):
            for j in range(i+1, len_list):
                if nums[i] + nums[j] == target:
                    indx_list.append(i)
                    indx_list.append(j)
                    brk_loop = True
                    break
            if brk_loop:
                break

        return indx_list


s1 = Solution_01()
print(s1.twoSum([2,7,11,15], 9))
