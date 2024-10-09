class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ## Using hint in the question, we should find a subarray with the
        ## max num in the array, adn the longest subarray would be one in which
        ## this max num repeats the most continuosly
        max_len = 1
        curr_len = 0
        max_num = -1
        i = 0
        while i < len(nums):
            if nums[i] < max_num:
                curr_len = 1 ## reset
            elif nums[i] > max_num:
                max_num = nums[i]
                curr_len = 1 ## both current window and
                max_len = 1 ## max length are reset as we have new max_num
            else:
                ## when nums[i] == max_num
                if nums[i] == nums[i-1]:
                    curr_len += 1
                else:
                    curr_len = 1
                max_len = max(max_len,curr_len)
            i += 1
        return max_len