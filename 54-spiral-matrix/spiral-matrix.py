class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        result = []

        while top <= bottom and left <= right: 

            # top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
            
        return result


