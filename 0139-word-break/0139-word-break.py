class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True ## represents empty string

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                ## Early exit from inner loop incase we have already found 
                ## a substring which corresponds to a word in wordDict or 
                ## a word which can already be built using wordDict
                if dp[i]:
                    break
        return dp[0]