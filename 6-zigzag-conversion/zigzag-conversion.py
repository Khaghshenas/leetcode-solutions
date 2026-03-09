class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1 or len(s)<=numRows:
            return s

        rows = [""]*numRows
        going_down = False
        current_row = 0

        for c in s:
            rows[current_row] += c

            if current_row==0 or current_row==numRows-1:
                going_down = not going_down

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        result = "".join(rows)              
        return result

        