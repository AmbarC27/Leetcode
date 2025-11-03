class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        ans = float("inf")
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                ans = min(ans,r-l+1)
                curr_sum -= nums[l]
                l += 1
            r += 1
        return ans if ans != float("inf") else 0