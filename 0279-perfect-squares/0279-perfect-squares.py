class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        
        def numways(target):
            if dp[target] < float("inf"):
                return dp[target]
            highest_number_to_be_squared = math.floor(math.sqrt(target))
            if target == highest_number_to_be_squared ** 2:
                return 1
            for num in range(1,highest_number_to_be_squared + 1):
                dp[target] = min(dp[target],1 + numways(target - num**2))
            return dp[target]

        return numways(n)