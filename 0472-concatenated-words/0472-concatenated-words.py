class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words_set = set(words)
        for word in words:
            dp = [False]*(len(word) + 1)
            dp[0] = True
            words_set.remove(word)
            # for i in range(len(word)-1,-1,-1):
            #     for sub_word in words:
            #         if (i + len(sub_word)) <= len(word) and word[i:i+len(sub_word)] == sub_word and word != sub_word:
            #             dp[i] = dp[i + len(sub_word)]
            #             if dp[i]:
            #                 break
            # if dp[0]:
            #     ans.append(word)
            for r in range(1,len(word)+1):
                for l in range(r):
                    if word[l:r] in words_set:
                        dp[r] = dp[l]
                    if dp[r]:
                        break
            words_set.add(word)
            if dp[-1]:
                ans.append(word)
        return ans