class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # sorted_arr = sorted(arr)
        # chunks = 0
        # for i in range(len(arr)):
        #     if sorted(arr[:i+1]) == sorted_arr[:i+1]:
        #         chunks += 1
        # return chunks

        ## This approach is editorial 1 of Leetcode 769, which is the first
        ## question in this series of questions
        n = len(arr)
        max_left = [0] * n
        min_right = [0] * n
        
        max_left[0] = arr[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i])
        
        min_right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i])
        
        chunks = 0
        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                chunks += 1

        return chunks + 1
