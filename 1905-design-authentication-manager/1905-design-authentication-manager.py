class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.minheap = []
        self.token_to_ttl = {}
        heapq.heapify(self.minheap)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_to_ttl[tokenId] = currentTime + self.ttl
        heapq.heappush(self.minheap, (currentTime + self.ttl,tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_to_ttl:
            if currentTime < self.token_to_ttl[tokenId]:
                self.token_to_ttl[tokenId] = currentTime + self.ttl
                heapq.heappush(self.minheap, (currentTime + self.ttl,tokenId))


    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.minheap and self.minheap[0][0] <= currentTime:
            expiry_time, token = heapq.heappop(self.minheap)
            if expiry_time == self.token_to_ttl[token]:
                ## if heap entries are stale i.e the latest expiry_time 
                ## doesnt match what the heap is getting rid of
                del self.token_to_ttl[token]
        return len(self.token_to_ttl)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)