class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minheap = [num for num in nums]
        heapq.heapify(minheap)
        operations = 0
        ## Note you dont need to condition on length being greater than 2
        ## as the test cases are generated such that the min number will
        ## always reach or surpass k
        while minheap[0] < k:
            ## Assume x is smallest, y is 2nd smallest
            x = heapq.heappop(minheap)
            y = heapq.heappop(minheap)
            heapq.heappush(minheap,2*x + y)
            operations += 1
        return operations