class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            left_sum = prefix_sum - num
            right_sum = tot_sum - prefix_sum
            if right_sum == left_sum:
                return i
        return -1