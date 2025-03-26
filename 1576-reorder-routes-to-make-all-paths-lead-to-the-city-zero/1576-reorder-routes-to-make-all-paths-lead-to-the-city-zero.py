class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_dict = {}
        for u,v in connections:
            if u not in adj_dict:
                adj_dict[u] = [(v,1)]
            else:
                adj_dict[u].append((v,1))
            if v not in adj_dict:
                adj_dict[v] = [(u,0)]
            else:
                adj_dict[v].append((u,0))
        
        def dfs(city):
            traversal_cost = 0
            for nei, cost_to_nei in adj_dict[city]:
                if nei not in visited:
                    visited.add(nei)
                    traversal_cost += cost_to_nei + dfs(nei)
            return traversal_cost

        visited = set()
        visited.add(0)
        return dfs(0)