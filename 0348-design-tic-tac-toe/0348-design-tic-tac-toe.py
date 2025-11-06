class TicTacToe:

    def __init__(self, n: int):
        ## For a player to win, either an entire row has to be theirs,
        ## an entire column or the negative or positive diagonal
        self.n = n
        self.rows = [[0]*n for _ in range(2)]
        self.cols = [[0]*n for _ in range(2)]
        self.neg_diag = [0,0]
        self.pos_diag = [0,0]

    def move(self, row: int, col: int, player: int) -> int:
        if row == col:
            ## On positive diagonal
            self.pos_diag[player-1] += 1
        if row + col == self.n - 1:
            self.neg_diag[player-1] += 1

        self.rows[player-1][row] += 1
        self.cols[player-1][col] += 1

        ## Check for winning conditions
        if self.pos_diag[player-1] == self.n or self.neg_diag[player-1] == self.n or self.rows[player-1][row] == self.n or self.cols[player-1][col] == self.n:
            return player 
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)