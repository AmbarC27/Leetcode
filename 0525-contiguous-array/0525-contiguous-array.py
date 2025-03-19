class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_arr = []
        prefix_sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            prefix_arr.append(prefix_sum)
        ## sum_to_idx holds the index where a number first appears in prefix_arr
        sum_to_idx = {}
        sum_to_idx[0] = -1
        ans = 0
        for i,prefix in enumerate(prefix_arr):
            if prefix not in sum_to_idx:
                sum_to_idx[prefix] = i
            else:
                ans = max(ans,i - sum_to_idx[prefix])
        return ans