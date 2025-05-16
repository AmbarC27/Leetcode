class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        components = 0
        visited = set()

        def dfs(i):
            visited.add(i)
            neighbors = adj_list[i]
            for neighbor in neighbors:
                if neighbor not in visited:
                    # visited.add(neighbor)
                    dfs(neighbor)

        print(adj_list)

        for i in range(n):
            if i not in visited:
                # visited.add(i)
                components += 1
                dfs(i)
        return components