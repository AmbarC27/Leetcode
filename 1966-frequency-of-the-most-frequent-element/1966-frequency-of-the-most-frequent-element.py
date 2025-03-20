class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        r = l = 0
        window_sum = 0 # holds sum of current window
        while r < len(nums):
            window_sum += nums[r]
            if (r-l+1)*nums[r] - window_sum > k:
                ## Number of operations required is greater than k
                window_sum -= nums[l]
                l += 1
            else:
                ans = max(ans,r-l+1)
            r += 1
        return ans
