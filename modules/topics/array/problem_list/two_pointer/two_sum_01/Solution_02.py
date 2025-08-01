from typing import List


class Solution_02:
    # Create buckets
    def hash_map_function(self, nums: List[int]):
        self.buckets = [[] for _ in range(len(nums))]
        len_buckets = len(self.buckets)

        for i in range(len(nums)):
            self.buckets[nums[i] % len_buckets].append((i, nums[i]))

    # Find second index
    def retrieve_bucket_item(self, find_value, current_index):
        len_buckets = len(self.buckets)
        for i, (k, v) in enumerate(self.buckets[find_value % len_buckets]):
            if v == find_value and k != current_index:
                return k
        return None

    # Find the list of two indices
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.hash_map_function(nums)

        for i in range(len(nums)):
            another_value = target - nums[i]
            second_index = self.retrieve_bucket_item(another_value, i)
            if (second_index is not None) and (i != second_index):
                return [i, second_index]


obj = Solution_02()
print(obj.twoSum([2222222, 2222222], 4444444))









