class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start or goal:
            start_parity = start & 1
            goal_parity = goal & 1
            count += int(start_parity != goal_parity)
            start = start >> 1
            goal = goal >> 1
        return count