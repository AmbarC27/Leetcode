class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()

        for src, neighbors in adj.items():
            ## Note len(neighbors) is same as indegree of a node
            ## (also same as outdegree coz its an undirected graph)
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)

        while leaves:
            ## It can be proven that there can only be max two centroids 
            ## i.e. nodes which give minimum height (proof below code)
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
    
## Proof by contradiction - Assume there exists a tree with three nodes, then
## one node has indegree = 2 and the other two have indegree of 1. Once the leaves of
## this tree are pruned we only have one node which is a centroid (gives minimum
## height). Similar argument can be made for a tree with four nodes. And trees with 
## n > 4 nodes can be reduced to the case of having three or four nodes too