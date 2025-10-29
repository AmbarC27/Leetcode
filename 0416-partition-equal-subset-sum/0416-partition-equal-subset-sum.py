class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2 == 1:
            return False

        subset_sum = tot_sum // 2
        
        ## As backtracking keeps track of two variables (remaining_sum
        ## and index, cache also needs to be two dimensional)
        cache = [[None] * (len(nums)) for _ in range(subset_sum+1)]

        def backtrack(remaining_sum,i,n):
            if remaining_sum < 0 or i == n:
                return False
            if remaining_sum == 0:
                ## the line below is (surprisingly) not required - makes sense
                ## as base cases don't necessarily need to cached
                cache[remaining_sum][i] = True
                return True
            if cache[remaining_sum][i] != None:
                return cache[remaining_sum][i]
            
            ## You can either decide to add element i to the current 
            ## subset which you are building, or omit it
            result = (backtrack(remaining_sum, i+1, n) or
                    backtrack(remaining_sum - nums[i], i+1, n))
            cache[remaining_sum][i] = result
            return result

        return backtrack(subset_sum, 0, len(nums))