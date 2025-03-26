from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        queue = deque()
        y,x = entrance
        steps = 0
        queue.append([y,x])
        maze[y][x] = 'v' ## v indicates visited cells
        while queue:
            curr_level = queue
            queue = collections.deque()
            steps += 1
            while curr_level:
                y,x = curr_level.popleft()

                for dy,dx in directions:
                    ny = y + dy
                    nx = x + dx

                    if 0 <= ny and ny < m and 0 <= nx and nx < n and maze[ny][nx] == '.':
                        if ny in [0,m-1] or nx in [0,n-1]:
                            return steps
                        else:
                            queue.append([ny,nx])
                            maze[ny][nx] = 'v'
                    
        return -1