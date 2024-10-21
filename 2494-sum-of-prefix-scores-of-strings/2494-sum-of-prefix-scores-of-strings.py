class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        scores = {}
        for word in words:
            curr_str = word[::] ## getting copy of the string
            while curr_str:
                if curr_str in scores:
                    scores[curr_str] += 1
                else:
                    scores[curr_str] = 1
                curr_str = curr_str[:-1]

        ans = []
        for word in words:
            score = 0
            for i in range(1,len(word)+1):
                score += scores[word[:i]]
            ans.append(score)

        return ans