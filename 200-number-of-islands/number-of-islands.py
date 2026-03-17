from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(-1 , 0), (1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    islands += 1
                    queue = deque([(i, j)])
                    visited.add((i, j))

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in directions:
                            x_1, y_1 = x + dx, y + dy
                            if 0 <= x_1 < m and 0 <= y_1 < n and grid[x_1][y_1] == "1" and (x_1, y_1) not in visited:
                                queue.append((x_1, y_1))
                                visited.add((x_1, y_1))

        return islands  




