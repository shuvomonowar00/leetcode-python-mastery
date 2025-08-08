'''
    1431. Kids With the Greatest Number of Candies

    Algorithm with pseudocode
    -------------------------
    1.	bool_list: List[bool] = []
    2.	max_candies = max(candies)
    3.	for i in range(len(candies))
    4.	if candies[i]+extra_candies >= max_candies -> List[bool].append(true)
    5.	else List[bool].append(false)
    6.	return bool_list
'''

from typing import List


class Solution_01:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res_candies: List[bool] = []
        max_candies: int = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_candies:
                res_candies.append(True)
            else:
                res_candies.append(False)
        return res_candies


if __name__ == '__main__':
    obj = Solution_01()
    print(obj.kidsWithCandies([2,3,5,1,3], 3))
