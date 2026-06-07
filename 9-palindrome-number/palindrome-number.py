class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_rev = 0
        x_orig = x

        while x:
            x_rev = x_rev * 10 + x % 10
            x = x // 10
        
        return x_orig == x_rev