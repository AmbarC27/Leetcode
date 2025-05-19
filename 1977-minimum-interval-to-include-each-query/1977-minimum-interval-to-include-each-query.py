class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        sorted_queries = sorted(queries)
        ans_dict = {}

        minheap = []
        heapq.heapify(minheap)
        i = 0

        for query in sorted_queries:
            ## Push intervals into the heap as long as its start point is
            ## lesser than or equal to the query
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                ## Add end point of interval into the heap too as that will
                ## be used to pop invalid intervals in the next block of code
                heapq.heappush(minheap,(r-l+1,r))
                i += 1

            ## Pop invalid intervals i.e. intervals whose end point
            ## is lesser than query
            while minheap and minheap[0][1] < query:
                heapq.heappop(minheap)

            ## If minheap is not empty that means there are intervals which 
            ## contain query, and thus choose the min length interval. If not,
            ## then return -1 as the question asks
            ans_dict[query] = minheap[0][0] if minheap else -1

        return [ans_dict[q] for q in queries]