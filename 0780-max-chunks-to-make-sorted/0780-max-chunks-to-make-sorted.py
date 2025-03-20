class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_in_current_chunk = -1
        for i in range(len(arr)):
            max_in_current_chunk = max(max_in_current_chunk,arr[i])
            if i == max_in_current_chunk:
                chunks += 1
                max_in_current_chunk = -1
        return chunks