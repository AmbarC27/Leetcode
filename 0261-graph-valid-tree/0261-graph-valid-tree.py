class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## Tree is supposed to have (n-1) edges
        if len(edges) != n - 1:
            return False
        ## We have ensured that we have either a forest or a graph
        ## (with cycles). Now if we can visit all the nodes from a
        ## particular node, then that means we have a connected tree 
        ## otherwise we have disconnected components (which don't 
        ## form a tree)
        adj_list = {i:[] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        nodes_visited = []
        visited = set()

        def dfs(i):
            visited.add(i)
            ## Could have also had added to visited set when iterating over 
            ## the neighbors, however in this case it doesn't matter where we 
            ## add to visited set as we aren't keeping any count
            ## If we did add to the visited set while iterating over the neighbors,
            ## then we would need to initate visited set with node 0 (starting node)
            ## even before we start DFS

            neighbors = adj_list[i]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)
        return len(visited) == n