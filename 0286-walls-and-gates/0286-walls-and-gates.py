class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms) ## j
        n = len(rooms[0]) ## i
        inf = 2147483647

        def bfs(i,j):
            visited = set()
            visited.add((i,j))
            next_level = collections.deque()
            next_level.append([i,j])
            curr_dist = 0
            while next_level:
                curr_level = next_level
                next_level = collections.deque()
                while curr_level:
                    x,y = curr_level.popleft()
                    rooms[y][x] = min(rooms[y][x],curr_dist)
                    # visited.add((x,y)) -> for questions which require maintaining
                    # some sort of count, never process at this stage
                    for dx,dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and rooms[ny][nx] not in [-1,0]:
                            next_level.append([nx,ny])
                            visited.add((nx,ny))
                curr_dist += 1
        
        for i in range(n):
            for j in range(m):
                if rooms[j][i] == 0:
                    bfs(i,j)
        