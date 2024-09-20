class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        island_num = 2 ## don't start from 0 or 1 to avoid confusion as
        ## cells would be changed in place
        # visited = set()
        islands = {}
        m = len(grid1)
        n = len(grid1[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for j in range(m):
            for i in range(n):
                if grid2[j][i] == 1: ## i.e. unvisited
                    queue = deque()
                    queue.append([i,j])
                    grid2[j][i] = island_num ## tagging it as visited
                    islands[island_num] = [[i,j]]
                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in directions:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid2[ny][nx] == 1:
                                grid2[ny][nx] = island_num ## tagging it as visited
                                queue.append([nx,ny])
                                islands[island_num].append([nx,ny])
                    island_num += 1
        print(islands)
        ans = 0
        for island in islands.keys():
            cells = islands[island]
            is_subisland = True
            for x,y in cells:
                if grid1[y][x] != 1:
                    is_subisland = False
                    break
            ans += int(is_subisland)
        return ans
