class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) <= numRows or numRows == 1:
            return s

        rows_val = ["" for _ in range(numRows)]

        current_row = 0
        to_down = True
        
        for c in s:
            rows_val[current_row] += c

            if current_row == 0:
                to_down = True
            elif current_row == numRows - 1:
                to_down = False
            
            if to_down:
                current_row += 1
            else:
                current_row -= 1

        res = ""
        for r in rows_val:
            res = res + r

        return res

