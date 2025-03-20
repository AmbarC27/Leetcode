class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ## Note for this question we could have also used a monotonically
        ## increasing stack, whereby each number in the stack would represent
        ## the minimum element in each chunk (not max as suggested by editorial
        ## 3). Thus the stack contains one number from each chunk, and so number
        ## of chunks equals length of stack

        chunks = 0
        max_in_current_chunk = -1

        ## We want that in the array range(beginning of chunk,end of chunk) we
        ## have all the numbers in the range(beginning of chunk,end of chunk).
        ## Every time we accomplish that, we have found a new chunk
        for i in range(len(arr)):
            max_in_current_chunk = max(max_in_current_chunk,arr[i])
            if i == max_in_current_chunk:
                chunks += 1
                max_in_current_chunk = -1
        return chunks