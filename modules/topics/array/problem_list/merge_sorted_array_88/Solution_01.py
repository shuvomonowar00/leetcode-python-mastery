from typing import List


class Solution_01:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        # Using for loop
        # for i in range(m, m+n):
        #     nums1[i] = nums2[j]
        #     j += 1
        # Using while loop
        e = m+n
        while m < e:
            nums1[m] = nums2[j]
            m += 1
            j += 1
        nums1.sort()
        print(nums1)


obj = Solution_03()
obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

        