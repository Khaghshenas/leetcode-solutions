class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        #x_1 = 0
        #while x:
        #    d = x%10
        #    x //= 10
        #    x_1 = 
        s = str(x)
        return s == s[::-1]
        