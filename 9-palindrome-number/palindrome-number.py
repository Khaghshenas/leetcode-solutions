class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_1 = 0
        num = x

        while num:
            x_1 = x_1*10 +num%10
            num //= 10
        
        return x == x_1
        
        