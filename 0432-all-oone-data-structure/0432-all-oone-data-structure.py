class AllOne:

    def __init__(self):
        self.map = {}
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def inc(self, key: str) -> None:
        self.map[key] = self.map.get(key,0) + 1
        heapq.heappush(self.minheap, (self.map[key],key))
        heapq.heappush(self.maxheap, (-1*self.map[key],key))

    def dec(self, key: str) -> None:
        self.map[key] -= 1
        if self.map[key] == 0:
            del self.map[key]
        else:
            heapq.heappush(self.minheap, (self.map[key],key))
            heapq.heappush(self.maxheap, (-1*self.map[key],key))

    def getMaxKey(self) -> str:
        if not self.maxheap:
            return ""
        while self.maxheap:
            count, key = self.maxheap[0]
            if key in self.map and self.map[key] == -1 * count:
                ## valid entry
                return key
            heapq.heappop(self.maxheap)  # remove stale entry
        return ""

    def getMinKey(self) -> str:
        if not self.minheap:
            return ""
        while self.minheap:
            count, key = self.minheap[0]
            if key in self.map and self.map[key] == count:
                ## valid entry
                return key
            heapq.heappop(self.minheap)  # remove stale entry
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()