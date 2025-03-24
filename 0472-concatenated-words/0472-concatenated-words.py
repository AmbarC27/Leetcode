class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words_set = set(words)
        for word in words:
            dp = [False]*(len(word) + 1)
            dp[0] = True ## Set empty substring as true as you can always form it
            
            ## Remove the current word from the set as otherwise we will always process
            ## that the current word is a substring of itself and fasely append to ans
            words_set.remove(word)
            for r in range(len(word)+1):
                for l in range(r):
                    if word[l:r] in words_set:
                        dp[r] = dp[l]
                    if dp[r]:
                        break
            
            ## Add the word back once processing is done
            words_set.add(word)
            if dp[-1]:
                ans.append(word)
        return ans