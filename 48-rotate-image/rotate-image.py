class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0 or n != len(matrix[0]):
            raise ValueError("Matrix must be N by N")
        
        layers = n//2

        for layer in range(layers):

            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                # save top row in top
                top = matrix[first][i]

                # replace top row with left col
                matrix[first][i] = matrix[last - offset][first]
                
                # replace left col with bottom row
                matrix[last - offset][first] = matrix[last][last - offset]

                # replace bottom row with right col
                matrix[last][last - offset] = matrix[i][last]
            
                # replace right col with top 
                matrix[i][last] = top

#return [list(reversed(col)) for col in zip(*matrix)]

        