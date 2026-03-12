from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # down, up, right, left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i, j) not in visited:
                    islands += 1
                    queue = deque([(i,j)])
                    visited.add((i, j))

                    while queue:
                        x, y = queue.popleft()
                        
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < rows and 0 <= ny < cols 
                                and grid[nx][ny] == "1" 
                                and (nx, ny) not in visited):
                                queue.append((nx, ny))
                                visited.add((nx, ny))

        return islands

        