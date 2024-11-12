class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        subset_sum = tot_sum // 2

        dp = [[-1]*(len(stones)+1) for _ in range(subset_sum+1)]
        def memoize(remaining_sum,idx):
            if idx == len(stones):
                return 0
            if dp[remaining_sum][idx] != -1:
                return dp[remaining_sum][idx]
            
            skip = memoize(remaining_sum, idx+1)
            dp[remaining_sum][idx] = skip

            if stones[idx] <= remaining_sum:
                include = stones[idx] + memoize(remaining_sum - stones[idx], idx+1)
                dp[remaining_sum][idx] = max(skip,include)
            return dp[remaining_sum][idx]

        subtraction_sum = memoize(subset_sum, 0)
        print(subtraction_sum)
        addition_sum = tot_sum - subtraction_sum
        return addition_sum - subtraction_sum

        