class SmallestInfiniteSet:

    def __init__(self):
        self.non_heap_num = 1
        minheap = []
        heapq.heapify(minheap)
        self.minheap = minheap
        ## Initiated to ensure duplicate numbers are not added in minheap
        self.nums_in_minheap = set()

    def popSmallest(self) -> int:
        if not self.minheap:
            smallest_num = self.non_heap_num
            self.non_heap_num += 1
        else:
            smallest_num = heapq.heappop(self.minheap)
            self.nums_in_minheap.remove(smallest_num)
        return smallest_num

    def addBack(self, num: int) -> None:
        ## Ensure to not add duplicate values in the minheap
        if num < self.non_heap_num and num not in self.nums_in_minheap:
            heapq.heappush(self.minheap,num)
            self.nums_in_minheap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)