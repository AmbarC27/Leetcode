class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # Sort words by length
        dp = {}  # dp[word] = longest chain ending with 'word'

        max_chain = 1
        for word in words:
            dp[word] = 1  # Every word is at least a chain of length 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]  # remove one char
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            max_chain = max(max_chain, dp[word])

        return max_chain