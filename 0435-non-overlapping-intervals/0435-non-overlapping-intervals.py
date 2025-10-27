class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x: x[0])
        # ans = [intervals[0]]
        # res = 0
        # i = 1
        # while i < len(intervals):
        #     ## No overlap
        #     if ans[-1][1] <= intervals[i][0]:
        #         ans.append(intervals[i])
        #         i += 1
        #     else:
        #         ## Overlap
        #         if ans[-1][1] > intervals[i][1]:
        #             ## Remove previous interval
        #             ans[-1] = intervals[i]
        #         else:
        #             ## Keep previous interval, no need to add current interval
        #             pass
        #         res += 1
        #         i += 1
        # return res

        ## Another approach is to sort by end time
        intervals = sorted(intervals, key = lambda x:x[1])
        last_interval = intervals[0]
        count = 0
        for i in range(1,len(intervals)):
            interval_start, interval_end = intervals[i]
            ## Overlap, so you remove the current interval
            if interval_start < last_interval[-1]:
                count += 1
            else:
                last_interval = intervals[i]
        return count

        ## The advantage of sorting by end time is that you already know which
        ## end time (last interval vs current interval) is bigger/smaller, and 
        ## so it's straightforward to assign last_interval_end before moving on
        ## to the next iteration. Look at neetcode's solutions (on sorting by
        ## start time vs end time) to see how it is easier to update when sorted 
        ## by end time rather than start time


        