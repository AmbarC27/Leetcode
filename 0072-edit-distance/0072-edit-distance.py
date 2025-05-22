class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## In DP table, row i represents ith char of word1, jth column 
        ## represents jth char of word2
        cache = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]
        for j in range(len(word1)+1):
            cache[j][-1] = len(word1) - j
        for i in range(len(word2)+1):
            cache[-1][i] = len(word2) - i

        ## Remember word2 is the target
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if word1[j] == word2[i]:
                    ## If chars are the same, no editing needs to be done on 
                    ## current char and thus only operations on word1[j+1:]
                    ## and word2[i+1:] are relevant
                    cache[j][i] = cache[j+1][i+1]
                else:
                    cache[j][i] = 1 + min(
                        cache[j][i+1], ## insert -> add char to current index and focus on next char in target string (word2)
                        cache[j+1][i], ## delete -> remove char from current index and hop onto the next char, while keeping target string index the same
                        cache[j+1][i+1]) ## replace ->move to the next indices

        return cache[0][0]