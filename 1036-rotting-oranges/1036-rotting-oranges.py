class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        initial_positions = []
        fresh_count = 0
        visited = set()

        for j in range(m):
            for i in range(n):
                if grid[j][i] == 2:
                    initial_positions.append([i,j])
                elif grid[j][i] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        print(fresh_count)
        
        time = -1
        next_level = collections.deque()
        for x,y in initial_positions:
            next_level.append([x,y])
            visited.add((x,y))
        # fresh_count += len(initial_positions)

        while next_level:
            curr_level = next_level
            next_level = collections.deque()
            # time += 1
            while curr_level:
                x,y = curr_level.popleft()
                # visited.add((x,y))
                grid[y][x] = 2
                # fresh_count -= 1
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < n) and (0 <= ny < m) and grid[ny][nx] == 1:
                        next_level.append([nx,ny])
                        # visited.add((nx,ny))
                        grid[ny][nx] = 2
                        fresh_count -= 1
            print(fresh_count)
            time += 1
        
        print(fresh_count)
        if fresh_count == 0:
            return time
        
        return -1