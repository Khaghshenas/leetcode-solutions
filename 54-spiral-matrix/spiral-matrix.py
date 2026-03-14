class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = []

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        
        while top <= bottom and left <= right:

            #top row
            for col in range(left, right + 1):
                output.append(matrix[top][col])
            top += 1

            #right col
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                #bottom row
                for col in range(right, left - 1, -1):
                    output.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                #left col
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1
        
        return output



        