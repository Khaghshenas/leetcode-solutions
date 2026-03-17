class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest = 0
        left = 0
        seen = {}

        for right, c in enumerate(s):
            if c in seen and left <= seen[c]:
                left = seen[c] + 1
            seen[c] = right
            
            longest = max(longest, right - left + 1)

        return longest

        
            


