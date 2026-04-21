class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        if n <= 1:
            return None
        
        seen = {}

        for i, num in enumerate(nums):
            num_1 = target - num    
            if num_1 in seen:
                return i, seen[num_1]
            seen[num] = i


        
        
