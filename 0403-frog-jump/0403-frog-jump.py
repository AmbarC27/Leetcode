class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[:2] != [0, 1]:
            return False

        stone_set = set(stones)
        ## dp[stone] holds the set of jump lengths through which the frog
        ## can reach the stone with value stone
        dp = {stone: set() for stone in stones}
        dp[1].add(1)

        for stone in stones:
            for jump in dp[stone]:
                for jump_length in [jump - 1, jump, jump + 1]:
                    if jump_length > 0 and (stone + jump_length) in stone_set:
                        dp[stone + jump_length].add(jump_length)

        ## If frog can reach the last stone, then the length of dp[stones[-1]]
        ## must be greater 0 as dp[stones[-1]] holds the jump length via which
        ## stones[-1] could be reached
        return len(dp[stones[-1]]) > 0