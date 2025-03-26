class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        for col in range(n):
            memo[(n-1,col)] = matrix[-1][col]

        def falling(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row == n - 1:
                return memo[(row,col)]
            else:
                curr_cell = matrix[row][col]
                min_cost = curr_cell + falling(row+1, col)
                if col > 0:
                    min_cost = min(min_cost,curr_cell + falling(row+1, col-1))
                if col < n - 1:
                    min_cost = min(min_cost,curr_cell + falling(row+1, col+1))
                memo[(row,col)] = min_cost
                return memo[(row,col)]

        ans = float("inf")
        for col in range(n):
            ans = min(ans,falling(0,col))
        return ans