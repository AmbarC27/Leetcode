class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # target = grid[-1][-1]
        # directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # t = grid[0][0]
        # while True:
        #     x = 0
        #     y = 0
        #     visited = set()
        #     next_level = collections.deque()
        #     next_level.append([0,0])
        #     visited.add((0,0))
        #     while next_level:
        #         curr_level = next_level
        #         next_level = collections.deque()
        #         while curr_level:
        #             x,y = curr_level.popleft()
        #             if grid[y][x] == target:
        #                 return t
        #             for dx,dy in directions:
        #                 nx = x + dx
        #                 ny = y + dy
        #                 if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited and grid[ny][nx] <= t:
        #                     next_level.append([nx,ny])
        #                     visited.add((nx,ny))
        #     t += 1

        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            # visit.add((r,c)) -> we can't add to visit here, otherwise
            ## we get TLE (read below)
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

        ## In this question t is monotonically increasing (or non-decreasing
        ## to be very specific) and so we will never come back to the same 
        ## cell again and get a better answer. That is why we do the visited
        ## check while looking for a cell's neighbor as we should never visit
        ## a cell which has already been processed