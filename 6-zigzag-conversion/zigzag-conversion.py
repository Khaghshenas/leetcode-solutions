class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) <= numRows or numRows == 1:
            return s

        rows = ["" for _ in range(numRows)]

        current_row = 0
        going_down = True
        
        for c in s:
            rows[current_row] += c

            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        res = "".join(rows)

        return res

