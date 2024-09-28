class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m_sum = sum(rolls)
        remaining_sum = mean*(m+n) - m_sum

        if remaining_sum > 6*n:
            return []
        elif remaining_sum < n:
            return []
        
        rolls_remaining = n
        ans = []
        while rolls_remaining > 0:
            avg_remaining_roll = remaining_sum / rolls_remaining
            roll_needed = math.ceil(avg_remaining_roll)
            ans.append(roll_needed)
            rolls_remaining -= 1
            remaining_sum -= roll_needed
        return ans