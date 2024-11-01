class MedianFinder:

    def __init__(self):
        self.maxheap = [] ## stores smaller values
        self.minheap = [] ## stores bigger values
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1*num)
        if (self.maxheap and self.minheap and 
            (-1 * self.maxheap[0]) > self.minheap[0]):
            ## case of inbalance within the two heaps
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        elif len(self.maxheap) + 1 < len(self.minheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*val)

        # heapq.heappush(self.minheap,num)
        # balance_val = heapq.heappop(self.minheap)
        # heapq.heappush(self.maxheap, -1*balance_val)

        # if len(self.minheap) < len(self.maxheap):
        #     balance_val = -1*heapq.heappop(self.maxheap)
        #     heapq.heappush(self.minheap, balance_val)
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        else:
            return 0.5 * (-1* self.maxheap[0] + self.minheap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()