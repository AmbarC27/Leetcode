class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_dict = {}
        for source,dest,cost in flights:
            if source not in adj_dict:
                adj_dict[source] = [[dest,cost]]
            else:
                adj_dict[source].append([dest,cost])

        costs = [float("inf")] * n
        next_level = collections.deque()
        next_level.append([src,0])
        stops = 0
        while next_level and stops <= k:
            curr_level = next_level
            next_level = collections.deque()
            # stops += 1
            while curr_level:
                airport,curr_cost = curr_level.popleft()
                if airport not in adj_dict:
                    continue
                for next_airport,next_cost in adj_dict[airport]:
                    if curr_cost + next_cost < costs[next_airport]:
                        costs[next_airport] = curr_cost + next_cost
                        next_level.append([next_airport,costs[next_airport]])
            stops += 1

        if costs[dst] == float('inf'):
            return -1
        return costs[dst]

