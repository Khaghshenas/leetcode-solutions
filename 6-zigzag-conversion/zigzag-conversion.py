class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        n = len(s)
        if n <= numRows or numRows == 1:
            return s
        
        matrix = [["" for _ in range(n)] for _ in range(numRows)]

        row = col = 0 
        to_down = True

        for c in s:
            matrix[row][col] = c

            if row == numRows - 1:
                to_down = False
            elif row == 0:
                to_down = True

            if to_down:
                row += 1
            else:
                row -= 1
                col += 1
        
        res = ""
        for r in matrix:
            res += ''.join(r)

        return res