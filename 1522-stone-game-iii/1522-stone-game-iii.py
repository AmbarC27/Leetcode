class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {} ## idx -> highest score of alice

        ## The way we are computing score is that the score from a future turn
        ## (i.e. with greater index than idx) is subtracted from the score on
        ## the present turn. So we will get a sequence of alternate turns between
        ## Alice and Bob
        def score(idx):
            if idx in dp:
                return dp[idx]
            if idx >= len(stoneValue):
                return 0
            score_of_player = max(
                stoneValue[idx] - score(idx+1),
                sum(stoneValue[idx:idx+2]) - score(idx+2),
                sum(stoneValue[idx:idx+3]) - score(idx+3)
            )
            dp[idx] = score_of_player
            return dp[idx]

        alices_score = score(0)
        print(dp)
        if alices_score > 0:
            return "Alice"
        elif alices_score < 0:
            return "Bob"
        else:
            return "Tie"