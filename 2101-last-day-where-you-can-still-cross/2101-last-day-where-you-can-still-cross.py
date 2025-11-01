import collections

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row ## (y) -> vertical
        m = col ## (x) -> horizontal

        def can_reach(blocked):
            queue = collections.deque()
            visited = set()
            for col in range(m):
                if not blocked[0][col]:
                    queue.append([0,col]) ## [row_num(y),col_num(x)]
                    visited.add((0,col)) ## [row_num(y),col_num(x)]
            while queue:
                r,c = queue.popleft()
                if r == n - 1:
                    return True
                for dr,dc in [[1,0],[-1,0],[0,-1],[0,1]]:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nc < m) and (0 <= nr < n) and (nr,nc) not in visited and not blocked[nr][nc]:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            return False

        def possible(mid):
            # build boolean blocked grid for the first mid+1 flooded cells
            blocked = [[False]*m for _ in range(n)]
            for r0, c0 in cells[:mid+1]:
                blocked[r0][c0] = True
            # single multi-source BFS from the open top row cells
            return can_reach(blocked)

        ans = 0
        cells = [(r - 1, c - 1) for r, c in cells]
        l = 0
        r = len(cells) - 1
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if possible(mid):
                ans = mid + 1 ## days are 1-indexed thus return mid + 1
                l = mid + 1
            else:
                r = mid -1 
        return ans
