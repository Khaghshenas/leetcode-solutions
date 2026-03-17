class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        else:
            pass
        

        MAX_32_INT = 2**31 - 1
        MIN_32_INT = -2**31
        
        
        digits = {'0': 0, 
                  '1': 1, 
                  '2': 2, 
                  '3': 3, 
                  '4': 4, 
                  '5': 5, 
                  '6': 6, 
                  '7': 7, 
                  '8': 8, 
                  '9': 9}
        
        res = 0
        begining = True

        for c in s:
            if begining and c=='0':
                continue
            begining = False
            if c in digits:
                res = res*10 + digits[c]
            else:
                break

        res = sign * res

        if res > MAX_32_INT:
            res = MAX_32_INT
        if res < MIN_32_INT:
            res = MIN_32_INT
        
        return res
        
        