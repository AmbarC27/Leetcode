class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city,visited):
            # visited.add(city)
            connections = isConnected[city]
            for i in range(len(connections)):
                nei = connections[i]
                if nei == 1 and i not in visited:
                    visited.add(i)
                    dfs(i,visited)
        
        ## Think of this as doing a floodfill of visited on the graph
        ## to mark visited nodes
        components = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                components += 1
                dfs(i,visited)
        return components