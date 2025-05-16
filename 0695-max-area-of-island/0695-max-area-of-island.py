class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) ## vertical
        n = len(grid[0]) ## horizontal
        max_area = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] == 1:
                    queue = collections.deque()
                    queue.append([i,j])
                    area = 0
                    grid[j][i] = 0 ## marking it so that we dont process it again
                    while queue:
                        # area += 1 ## can increment area either before or after processing
                        x,y = queue.popleft()
                        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                            nx = x + dx
                            ny = y + dy
                            if (0 <= nx < n) and (0 <= ny < m) and grid[ny][nx] == 1:
                                queue.append([nx,ny])
                                grid[ny][nx] = 0 ## marking it so that we dont process it again
                        area += 1
                    max_area = max(max_area,area)
        return max_area
