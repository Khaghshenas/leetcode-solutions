class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # If this sum is closer to target, update closest_sum
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                # Move pointers based on comparison with target
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # Exact match found
                    return total

        return closest_sum