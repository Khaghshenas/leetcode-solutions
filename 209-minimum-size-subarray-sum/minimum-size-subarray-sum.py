class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        min_length = float('inf')

        left, current_sum = 0, 0
    
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target and left <= right:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        
        return min_length if min_length != float('inf') else 0

                




        
        


