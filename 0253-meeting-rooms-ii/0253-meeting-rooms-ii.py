class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # First approach (more intuitive)
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        minheap = []
        heapq.heapify(minheap)
        # heapq.heappush(minheap,intervals[0][1])
        ans = 1
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            while minheap and minheap[0] <= curr_start:
                heapq.heappop(minheap)
            heapq.heappush(minheap,curr_end)
            ans = max(ans,len(minheap))
        return ans

        ## Second approach
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        ans = 0
        curr_count = 0
        s = 0
        e = 0
        print(start)
        print(end)
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                curr_count += 1
            elif start[s] >= end[e]:
                e += 1
                curr_count -= 1
            ans = max(ans,curr_count)
        return ans