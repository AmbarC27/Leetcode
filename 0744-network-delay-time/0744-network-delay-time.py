class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        for u,v,w in times:
            adj[u].append([v,w])
            
        shortest_dist = {} ## {node:shortest_distance_from_source}
        minheap = [[0,k]] ## node weight from k to itself is 0
        while minheap:
            weight,node  = heapq.heappop(minheap)
            if node in shortest_dist:
                continue
            ## Case when node has not been visited yet
            shortest_dist[node] = weight
                
            for new_node,new_weight in adj[node]:
                if new_node not in shortest_dist:
                    heapq.heappush(minheap,[weight+new_weight,new_node])
                    
        if len(shortest_dist) == n:
            return max(shortest_dist.values())
        else:
            return -1
        