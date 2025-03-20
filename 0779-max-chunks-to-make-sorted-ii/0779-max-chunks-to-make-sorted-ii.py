class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        ## Need a monotonic non-decreasing stack
        # stack = []
        # for i in range(len(arr)):
        #     while stack and stack[-1] >= arr[i]:
        #         stack.pop()
        #     stack.append(arr[i])
        # return len(stack)
        chunks = 0
        for i in range(len(arr)):
            if sorted(arr[:i+1]) == sorted_arr[:i+1]:
                chunks += 1
        return chunks