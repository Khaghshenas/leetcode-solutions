class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0 

        roman_map = {'M': 1000,
                     'D': 500, 
                     'C': 100,
                     'L': 50, 
                     'X': 10,
                     'V': 5,
                     'I': 1}
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and (roman_map[s[i]] < roman_map[s[i+1]]):
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total