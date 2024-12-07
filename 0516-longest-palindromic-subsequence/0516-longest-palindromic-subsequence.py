class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        def helper(l,r):
            if dp[l][r] != -1:
                return dp[l][r]
            if l > r:
                dp[l][r] = 0
                return dp[l][r]
            if l == r:
                dp[l][r] = 1
                return dp[l][r]
            if s[l] == s[r]:
                return 2 + helper(l+1,r-1)
            else:
                dp[l][r] = max(helper(l+1,r),helper(l,r-1))
                return dp[l][r]
        
        return helper(0,n-1)