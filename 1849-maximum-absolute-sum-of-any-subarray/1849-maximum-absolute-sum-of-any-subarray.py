class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pos = 0
        rolling_sum = 0
        for num in nums:
            rolling_sum += num
            if rolling_sum < 0:
                rolling_sum = 0
            else:
                max_pos = max(max_pos,rolling_sum)
        
        max_neg = 0
        rolling_sum = 0
        for num in nums:
            rolling_sum += num
            if rolling_sum > 0:
                rolling_sum = 0
            else:
                max_neg = min(max_neg,rolling_sum)

        return max(max_pos,abs(max_neg))