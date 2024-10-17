class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def validtree(edges):
            n = len(edges) + 1
            adj_list = {i:[] for i in range(1,n+1)}
            for x,y in edges:
                adj_list[x].append(y)
                adj_list[y].append(x)
            visited = set()
            def dfs(i):
                visited.add(i)
                for neighbor in adj_list[i]:
                    if neighbor not in visited:
                        dfs(neighbor)
            dfs(1) ## could have been any starting node
            
            return len(visited) == n

        # print(validtree(edges[:1] + edges[1:]))

        ans = []
        for i in range(len(edges)):
            curr_edges = edges[:i] + edges[i+1:]
            # print(curr_edges)
            if validtree(curr_edges):
                ans = edges[i]
        return ans