class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ## available starts as a sorted array, and a sorted array is a heap so we don't need
        ## to call heapify on it
        available = [i for i in range(n)]  # Min heap for available rooms
        used = []  # Min heap for rooms in use [(end_time, room_number)]
        count = [0] * n  # Count of meetings for each room

        for start, end in meetings:
            ## free up rooms where meeting has already ended
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            ## if no room available for meeting, the current will
            ## be delayed - reflected by updating end time
            if not available:
                end_time, room = heapq.heappop(used)
                ## meeting is delayed by duration of previous meeting
                end = end_time + (end - start) ## duration of meeting = (end - start)
                heapq.heappush(available, room)

            ## There is at least one room available for hosting
            ## a meeting
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))