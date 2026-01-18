'''
    Problem: 643. Maximum Average Subarray I
    Time Complexity: O()
    Space Complexity: O()
    Auxiliary Space: 
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg_val = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_avg_val = max(max_avg_val, window_sum/k)
        
        return max_avg_val