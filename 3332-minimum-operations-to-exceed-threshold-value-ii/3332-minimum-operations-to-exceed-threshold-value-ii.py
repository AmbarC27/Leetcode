class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minheap = [num for num in nums]
        heapq.heapify(minheap)
        operations = 0
        while minheap[0] < k and len(minheap) >= 2:
            ## Assume x is smallest, y is 2nd smallest
            x = heapq.heappop(minheap)
            y = heapq.heappop(minheap)
            heapq.heappush(minheap,2*x + y)
            operations += 1
        return operations