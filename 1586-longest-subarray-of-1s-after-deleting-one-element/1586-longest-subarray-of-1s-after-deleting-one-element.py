class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        window_sum = 0
        l = r = 0
        ans = 0
        while r < len(nums):
            window_sum += nums[r]
            while window_sum + 1 < (r-l+1):
                window_sum -= nums[l]
                l += 1
            ans = max(ans,window_sum)
            r += 1
        return ans