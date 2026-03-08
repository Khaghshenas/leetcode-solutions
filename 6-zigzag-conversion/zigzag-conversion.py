class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s

        row, col = 0, 0
        cols = len(s)
        going_down = True
        matrix = [["" for _ in range(cols)] for _ in range(numRows)]
        
        for c in s:
            matrix[row][col] = c

            if going_down:
                if row == numRows-1:
                    going_down = False
                    row -= 1
                    col +=1
                else:
                    row +=1
            else:
                if row == 0:
                    going_down = True
                    row +=1
                else:
                    row -= 1
                    col += 1

        result = ""
        for r in matrix:
            result += "".join(r)

        return result                

        