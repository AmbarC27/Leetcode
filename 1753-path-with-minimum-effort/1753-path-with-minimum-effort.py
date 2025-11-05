class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights[0])
        n = len(heights)
        visited = set()
        minheap = [(0,0,0)]
        heapq.heapify(minheap)

        while True:
            effort, r, c = heapq.heappop(minheap)
            if (r,c) == (n-1,m-1):
                return effort
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr,dc in [[1,0],[-1,0],[0,-1],[0,1]]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n) and (0 <= nc < m) and (nr,nc) not in visited:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(minheap,(max(effort,diff),nr,nc))
