class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## The heap holds the tasks that are ready to be processed, while the queue
        ## holds the tasks which are currently in their "cool-down" period
        counter = Counter(tasks)
        maxheap = [-count for count in counter.values()]
        heapq.heapify(maxheap)
        ## Queue empty initially means there are no tasks in cooldown period
        queue = collections.deque()

        ## Think of each loop iteration as three operations:
        ## 1) Increment time
        ## 2) heappop - Possibly execute one task (if heap not empty)
        ## 3) heappush - Possibly mark some cooling tasks as ready again for next time
        time = 0
        while maxheap or queue:
            ## During each time interval only one unit of work is done as there is only
            ## one heap pop operation
            time += 1
            if maxheap:
                ## In essence we are decreasing frequency. However as we are
                ## using a maxheap, increasing the number corresponds to decreasing it
                ## until it reaches 0
                freq = 1 + heapq.heappop(maxheap)
                ## if freq == 0, that means this particular task doesn't need to
                ## be processed anymore
                if freq != 0:
                    ## add the frequency and the time when cooldown period for the task
                    ## ends (not when the task is ready to be picked up again, that makes
                    ## the cases to handle a little trickier)
                    queue.append([freq,time+n])
            if queue:
                ## If queue[0][1] == time, that means the cooldown period of this particular
                ## task just ended, and so we move it back into the heap so it can
                ## be picked up in the next iteration.
                if queue[0][1] == time:
                    freq, _ = queue.popleft()
                    heapq.heappush(maxheap,freq)
        return time 