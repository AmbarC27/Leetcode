class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        prev_three_nums = [0,1,1] ## corresponds to T_(n-3),T_(n-2),T_(n-1)
        while n > 3:
            tribonacci_num = sum(prev_three_nums)
            prev_three_nums[0] = prev_three_nums[1]
            prev_three_nums[1] = prev_three_nums[2]
            prev_three_nums[2] = tribonacci_num
            n -= 1
        return sum(prev_three_nums)