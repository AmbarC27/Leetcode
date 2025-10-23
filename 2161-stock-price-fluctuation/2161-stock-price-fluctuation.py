class StockPrice:

    def __init__(self):
        self.records = {} ## timestamp -> price
        self.latest = 0
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        heapq.heappush(self.minheap,[price,timestamp])
        heapq.heappush(self.maxheap,[-price,timestamp])
        self.latest = max(self.latest,timestamp)

    def current(self) -> int:
        return self.records[self.latest]

    def maximum(self) -> int:
        heaptop_price, heaptop_time = self.maxheap[0]
        while self.records[heaptop_time] != -1*heaptop_price:
            ## case when record is outdated
            heapq.heappop(self.maxheap)
            heaptop_price, heaptop_time = self.maxheap[0]
        return -1 * heaptop_price

    def minimum(self) -> int:
        heaptop_price, heaptop_time = self.minheap[0]
        while self.records[heaptop_time] != heaptop_price:
            ## case when record is outdated
            heapq.heappop(self.minheap)
            heaptop_price, heaptop_time = self.minheap[0]
        return heaptop_price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()