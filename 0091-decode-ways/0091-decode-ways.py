class Solution:
    def numDecodings(self, s: str) -> int:
        ## DP approach where we are counting how many ways to decode for the
        ## string s[i:]. Our final answer is number of ways to decode s[0:] and
        ## thus dp[0]
        dp = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                ## s[i] is between 1 and 9
                dp[i] = dp[i+1]

                ## Condition checks if the next two strings in the sequence
                ## give a number <= 26
                if (i+1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                    dp[i] += dp[i+2]
        return dp[0]