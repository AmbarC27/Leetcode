class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## Create a complete graph of all the points
        adj_dict = {}
        for i in range(len(points)):
            for j in range(len(points)):
                nodes = []
                if i != j:
                    nodes.append(points[j])
            adj_dict[tuple(points[i])] = points
        ## In heap first value is the edge weight and second value is the 
        ## next node. Our initial next node would be the first node in points
        heap = [[0,points[0]]]
        heapq.heapify(heap)
        visited = set()
        total = 0
        while heap:
            weight,curr_node = heapq.heappop(heap)
            if tuple(curr_node) in visited:
                ## Node is already in MST, so skip it to avoid cycles
                continue
            
            ## Case when node is not in MST
            total += weight
            visited.add(tuple(curr_node))
            for next_node in adj_dict[tuple(curr_node)]:
                if tuple(next_node):
                    x1 = curr_node[0]
                    x2 = next_node[0]
                    y1 = curr_node[1]
                    y2 = next_node[1]
                    dist = abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,[dist,next_node])
        return total
