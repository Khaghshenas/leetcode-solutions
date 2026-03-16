class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        min_distance = float('inf')
        current_sum = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            
            left, right = i + 1, n - 1


            while left < right:
                total = nums[i] + nums[left] + nums[right]
                distance = abs(total - target)
                
                if distance < min_distance:
                    min_distance = distance
                    current_sum = total
                else:
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        return total   
                
        
        return current_sum


            