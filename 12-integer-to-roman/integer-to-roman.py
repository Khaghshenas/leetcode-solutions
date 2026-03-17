class Solution:
    def intToRoman(self, num: int) -> str:

        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
        
        roman_str = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman_str += symbols[i]
        
        return roman_str

        




        