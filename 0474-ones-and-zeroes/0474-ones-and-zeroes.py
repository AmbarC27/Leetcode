class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[idx][i][j] represents the max subsets with idx strings considered and i 0's and j 1's remaining
        dp = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]

        def memoize(curr_m, curr_n, idx):
            # Base case: if we've processed all strings
            if idx == len(strs):
                return 0

            # Return precomputed result if it exists
            if dp[idx][curr_m][curr_n] != -1:
                return dp[idx][curr_m][curr_n]

            # Count ones and zeroes in the current string
            count_one = strs[idx].count("1")
            count_zero = len(strs[idx]) - count_one

            # Option 1: Skip the current string
            skip = memoize(curr_m, curr_n, idx + 1)

            # Option 2: Include the current string if we have enough zeroes and ones
            include = -1
            if count_zero <= curr_m and count_one <= curr_n:
                include = 1 + memoize(curr_m - count_zero, curr_n - count_one, idx + 1)

            # Store the maximum result in dp table
            dp[idx][curr_m][curr_n] = max(skip, include)

            return dp[idx][curr_m][curr_n]

        # Star the recursive memoization with full capacities m and nt
        return memoize(m, n, 0)