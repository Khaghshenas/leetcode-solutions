class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        if n==0:
            return 0
        if n==1:
            return height[0]
        
        left = 0
        right = len(height)-1
        largets = 0
        
        while left < right:

            largets = max(largets, (right-left)*min(height[right], height[left]))
            if height[left]<=height[right]:
                left += 1
            else:
                right -=1
        
        return largets


        