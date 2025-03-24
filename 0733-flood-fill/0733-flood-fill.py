from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        m = len(image)
        n = len(image[0])
        queue = deque()
        queue.append([sr,sc])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        visited.add((sr,sc))
        while queue:
            y,x = queue.popleft()
            #visited.add((y,x))
            image[y][x] = color
            for dy,dx in dirs:
                ny = y + dy
                nx = x + dx
                if (0<=ny and ny < m) and (0 <= nx < n) and (ny,nx) not in visited and image[ny][nx] == start:
                    queue.append((ny,nx))
                    visited.add((ny,nx))
                    
        return image