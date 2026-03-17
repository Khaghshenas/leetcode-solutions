class Solution:
    def reverse(self, x: int) -> int:
        if x//10 == 0:
            return x
        
        if x < 0:
            sign = -1
        else:
            sign = 1

        MAX = 2**31 - 1
        MIN = -2**31

        num = x * sign
        x_rev = 0
        
        while num:
            if (x_rev * 10 + num%10) > MIN and (x_rev * 10 + num%10) < MAX:
                x_rev = x_rev * 10 + num%10
            else:
                return 0
            num = num//10

        return x_rev*sign
        
        