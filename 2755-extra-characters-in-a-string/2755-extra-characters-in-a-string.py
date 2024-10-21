class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float("inf")]*(n+1)
        dictionary = set(dictionary)

        ## extra(i:) measures min number of chars needed for s[i:]
        def extra(idx):
            if idx == n:
                return 0
            if dp[idx] != float("inf"):
                return dp[idx]
            ## Option 1: skip the current character and move on to the
            ## next character
            dp[idx] = 1 + extra(idx+1)

            ## Option 2: Look for words in dictionary starting from current idx
            for end in range(idx,n):
                word = s[idx:end+1]
                if word in dictionary:
                    dp[idx] = min(dp[idx],extra(end+1))
            return dp[idx]

        return extra(0)