class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        def number_of_neighbors(x,y):
            neighbors = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < m) and (0 <= ny < n) and grid[ny][nx] == 1:
                    neighbors += 1
            return neighbors

        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[j][i] == 1:
                    perimeter += (4 - number_of_neighbors(i, j))
        return perimeter