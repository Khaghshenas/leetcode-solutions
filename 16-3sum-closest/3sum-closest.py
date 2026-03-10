class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_distance = 2*(10**4)
        min_distance_sum = 2*(10**4)

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left<right:
                total = nums[i]+nums[left]+nums[right]
                distance = abs(total - target)
                
                if distance<=min_distance:
                        min_distance = distance
                        min_distance_sum = total

                if total==target:
                    return total
                elif total<target:
                    left += 1
                else:
                    right -= 1
        
        return min_distance_sum
        