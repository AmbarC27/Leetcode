class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_of_ones = sum(data)
        l = 0
        r = num_of_ones

        #ans = num_of_ones
        zeros_in_window = r - sum(data[l:r])
        ans = zeros_in_window
        while r < len(data):
            if data[r] == 0:
                zeros_in_window += 1
            if data[l] == 0:
                zeros_in_window -= 1
            l += 1
            r += 1
            ans = min(ans,zeros_in_window)
        return ans