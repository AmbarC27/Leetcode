class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        sorted_queries = sorted(queries)
        ans_dict = {}

        minheap = []
        heapq.heapify(minheap)
        i = 0

        ## Think of it as two steps:
        ## 1) Push all intervals which may potentially include query by putting all
        ## intervals whose start point is lesser than query (being overly optimistic)
        ## 2) Go from overly optimistic to realistic by removing all queries whose end
        ## point doesn't cover the query
        for query in sorted_queries:
            ## Push intervals into the heap as long as its start point is
            ## lesser than or equal to the query, and so the interval may 
            ## potentially contain query
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

            ## At this point the minheap will only contain intervals which
            ## contain query
            ans_dict[query] = minheap[0][0] if minheap else -1

        return [ans_dict[q] for q in queries]