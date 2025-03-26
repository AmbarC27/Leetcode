class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(curr_num,remaining_sum,remaining_nums,curr_combo):
            if remaining_nums == 0 and remaining_sum == 0:
                ans.append(curr_combo)
            elif remaining_nums == 0:
                ## Exhausted no. max allowed numbers but didn't reach sum
                return
            elif remaining_sum <= 0:
                ## Reached the sum before having k numbers, thus discard
                return
            
            for num in range(curr_num+1,9+1):
                new_combo = curr_combo + [num]
                backtrack(num, remaining_sum - num, remaining_nums - 1, new_combo)
        backtrack(0, n, k, [])
        return ans