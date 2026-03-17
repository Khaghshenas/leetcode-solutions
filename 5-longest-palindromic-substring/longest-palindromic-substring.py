class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        longest = ""
        for i in range(n):

            l = r = i
            
            while l >= 0 and r < n and s[l] == s[r]: 
                longest = s[l:r+1] if (r - l + 1) > len(longest) else longest
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                longest = s[l:r+1] if (r - l + 1) > len(longest) else longest
                l -= 1
                r += 1
            
        
        return longest

