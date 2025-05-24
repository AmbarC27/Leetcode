class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(2,1),(1,2),(-1,2),(-2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        next_level = collections.deque()
        next_level.append([0,0])
        visited = set()
        visited.add((0,0))
        ans = 0
        while next_level:
            curr_level = next_level
            next_level = collections.deque()
            while curr_level:
                curr_x, curr_y = curr_level.popleft()
                if curr_x == x and curr_y == y:
                    return ans
                for dx,dy in directions:
                    nx = curr_x + dx
                    ny = curr_y + dy
                    if (nx,ny) not in visited:
                        next_level.append([nx,ny])
                        visited.add((nx,ny))
            ans += 1
        return ans