class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words_set = set(words)
        for word in words:
            dp = [False]*(len(word) + 1)
            dp[-1] = True ## Set empty substring as true as you can always form it
            
            ## Remove the current word from the set as otherwise we will always process
            ## that the current word is a substring of itself and fasely append to ans
            words_set.remove(word)

            ## Either for loop works
            ## If this for loop changes, need to change lines 7 and 32
            # for r in range(len(word)+1):
            #     for l in range(r):
            #         if word[l:r] in words_set:
            #             dp[r] = dp[l]
            #         if dp[r]:
            #             break

            ## Either for loop works
            for l in range(len(word),-1,-1):
                for r in range(l+1,len(word)+1):
                    if word[l:r] in words_set:
                        dp[l] = dp[r]
                    if dp[l]:
                        break
            
            ## Add the word back once processing is done
            words_set.add(word)
            if dp[0]:
                ans.append(word)
        return ans