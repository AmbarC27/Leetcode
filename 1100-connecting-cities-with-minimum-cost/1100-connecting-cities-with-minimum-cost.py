class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(1,n+1)}
        for u,v,w in connections:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w])
        
        visited = set()
        heap = []
        heapq.heapify(heap)
        ## Let 1 be the starting node
        heapq.heappush(heap, [0,1]) ## node 1 with weight 0
        ans = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            ans += weight
            visited.add(node)
            for nei, nei_weight in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(heap,[nei_weight,nei])
        if len(visited) == n:
            return ans
        return -1
