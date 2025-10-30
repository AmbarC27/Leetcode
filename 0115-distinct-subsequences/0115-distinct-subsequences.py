class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {} ## cache[(i,j)] holds answer for s[i:] and t[j:]

        ## i iterates over s and j iterates over t
        def backtrack(i,j):
            ## if t is empty, there is only one subsequence (empty string) 
            ## which can be made out of s
            if j == len(t):
                return 1
            ## if s is empty, then no subsequence of s can equal t
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = backtrack(i+1,j+1) + backtrack(i+1,j)
            else:
                ## is s[i] and t[j] do not match, look at the next character in s
                ## trying to match current character in t
                cache[(i,j)] = backtrack(i+1,j)
            return cache[(i,j)]

        backtrack(0, 0)
        return cache[(0,0)]