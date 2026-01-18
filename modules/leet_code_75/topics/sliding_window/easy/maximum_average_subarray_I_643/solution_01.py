'''
    Problem: 643. Maximum Average Subarray I
    Time Complexity: O()
    Space Complexity: O()
    Auxiliary Space: 
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_avg_val = sum / k

        j = k
        for i in range(len(nums)):
            new_sum = sum
            if j < len(nums):
                new_sum += nums[j]
                sum = new_sum - nums[i]
                new_avg_sum = sum / k
                if new_avg_sum > max_avg_val:
                    max_avg_val = new_avg_sum
            else:
                break
            j += 1
        
        return max_avg_val





