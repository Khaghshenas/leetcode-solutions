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
            if (x_rev * 10 + num%10)*sign > MAX or (x_rev * 10 + num%10)*sign < MIN:
                return 0
            else:
                x_rev = x_rev * 10 + num%10
                num = num//10

        return x_rev*sign
        
        