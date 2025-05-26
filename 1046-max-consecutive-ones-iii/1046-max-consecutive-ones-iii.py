class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_sum = 0
        l = r = 0
        ans = 0
        while r < len(nums):
            window_sum += nums[r]
            while window_sum + k < (r-l+1):
                window_sum -= nums[l]
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans