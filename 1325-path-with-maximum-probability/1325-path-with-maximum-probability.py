class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)}
        for i in range(len(edges)):
            adj[edges[i][0]].append([edges[i][1],succProb[i]])
            adj[edges[i][1]].append([edges[i][0],succProb[i]])
        
        ## First solution - modified djikstra
        # max_prob = {} # maps node -> probability from source
        # maxheap = [[-1,start_node]] # all probs will be negative as heapq implementation always give minheaps
        # while maxheap:
        #     prob,node = heapq.heappop(maxheap)
        #     if node not in max_prob:
        #         max_prob[node] = prob

        #         for new_node,new_prob in adj[node]:
        #             if new_node not in max_prob:
        #                 heapq.heappush(maxheap,[prob*new_prob,new_node])
        # if end_node not in max_prob:
        #     return 0
        # else:
        #     return max_prob[end_node] * -1

        ## Second solution - almost djikstra but using queue instead of heap
        max_prob = [0]*n
        queue = deque()
        queue.append([start_node,1])
        while queue:
            node, prob_so_far = queue.popleft()
            for next_node,next_node_prob in adj[node]:
                if prob_so_far * next_node_prob > max_prob[next_node]:
                    max_prob[next_node] = prob_so_far * next_node_prob
                    queue.append([next_node,max_prob[next_node]])
        return max_prob[end_node]