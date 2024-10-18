class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## dp[i] holds longest increasing subsequence possible starting
        ## from index i 
        dp = [1] * len(nums) 
        ## Initialize all values as 1 as that is the smallest increasing 
        ## subsequence possible starting from each index 
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        
        return max(dp)