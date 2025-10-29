class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        # zeroes = set()
        # for j in range(m):
        #     for i in range(n):
        #         if matrix[j][i] == 0:
        #             zeroes.add((i,j))

        # def set_zero(x,y):
        #     nonlocal m,n 
        #     i = x
        #     while i >= 0:
        #         matrix[y][i] = 0
        #         i -= 1
        #     i = x
        #     while i < n:
        #         matrix[y][i] = 0
        #         i += 1
        #     i = y
        #     while i >= 0:
        #         matrix[i][x] = 0
        #         i -= 1
        #     i = y
        #     while i < m:
        #         matrix[i][x] = 0
        #         i += 1
        
        # for x,y in zeroes:
        #     set_zero(x, y)

        ## Second approach using O(1) space 

        ## If a row is supposed to be zero, we can flag it by setting the first 
        ## column of that row to 0. Same applies for columns that need to be
        ## zero where we set the first row to 0

        ## As there is an overlap in first row and first column (matrix[0][0]),
        ## we will maintain an additional variable for it
        rows = len(matrix)
        cols = len(matrix[0])

        rowzero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        rowzero = True
                    else:
                        matrix[r][0] = 0
        
        # def set_col_zero(c):
        #     nonlocal rows
        #     for r in range(rows):
        #         matrix[r][c] = 0

        # def set_row_zero(r):
        #     nonlocal cols
        #     for c in range(cols):
        #         matrix[r][c] = 0

        # for r in range(1,rows):
        #     if matrix[r][0] == 0:
        #         set_row_zero(r)
        # for c in range(1,rows):
        #     if matrix[0][c] == 0:
        #         set_col_zero(c)
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if rowzero:
            for c in range(cols):
                matrix[0][c] = 0