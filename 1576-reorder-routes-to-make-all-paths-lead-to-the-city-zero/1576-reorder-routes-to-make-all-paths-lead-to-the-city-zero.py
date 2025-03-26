class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ## Key to this question is that we create an undirected graph out
        ## of the initial directed graph. Original edges will have a cost 
        ## of 1 and the new edges will have a cost of 0. As we want to change
        ## roads which lead away from zero, we start traversing from zero
        ## (either BFS or DFS) and we find the cost to traverse the entire graph
        ## The original edges which lead away from zero will add 1 to the cost
        ## each time it is traversed 
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