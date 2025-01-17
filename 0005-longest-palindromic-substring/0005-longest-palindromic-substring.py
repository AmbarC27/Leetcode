class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0,0]
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]
        for diff in range(2,n):
            for l in range(n-diff):
                r = l + diff
                if s[l] == s[r] and dp[l+1][r-1]:
                    dp[l][r] = True
                    ans = [l,r]
        l,r = ans
        return s[l:r+1]