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
            elif nums[i] == max_num:
                ## Case when we are on a continuous streak of the max_num
                if nums[i] == nums[i-1]:
                    curr_len += 1
                else:
                    ## Case when we are seeing the max_num again after 
                    ## seeing some other number
                    curr_len = 1
                max_len = max(max_len,curr_len)
            i += 1
        return max_len