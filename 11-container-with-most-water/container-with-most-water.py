class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height)==0:
            return 0
        if len(height)==1:
            return height[0]
        
        l = 0
        r = len(height) - 1
        max_area = 0

        while r>l:

            max_area = max(max_area, (r-l)*min(height[l], height[r]))
            if height[l]<=height[r]:
                l += 1
            else:
                r -= 1

        return max_area  


        