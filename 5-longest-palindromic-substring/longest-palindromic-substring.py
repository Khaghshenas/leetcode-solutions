class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        longest = ""

        for i in range(n-1):
            for j in range(i, n):
                s_1 = s[i:j+1]

                """l, r = i, j
                while (l < r):
                    if s[l] != s[r]:
                        break
                    l += 1
                    r -= 1
                    """
                if s_1 == s_1[::-1]:    
                    longest = s_1 if len(s_1) > len(longest) else longest
        
        return longest

        

