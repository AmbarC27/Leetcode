class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)
        k = k % chalk_sum
        idx = 0
        while k >= chalk[idx]:
            k -= chalk[idx]
            idx  += 1
        return idx