from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        if self.get_first_blank(board) == (-1, -1):
            return True
        i, j = self.get_first_blank(board)
        for value in range(1, 10):
            board[i][j] = str(value)
            if self.check_valid(board, i, j):
                if self.solve(board):
                    return True
        board[i][j] = '.'
        return False


    def get_first_blank(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def check_valid(self, board, i, j):
        row = board[i]
        coloum = [board[x][j] for x in range(9)]
        square = [board[x][y] for x in range(i//3*3, i//3*3+3) for y in
                  range(j//3*3, j//3*3+3)]
        if row.count(board[i][j]) > 1 or coloum.count(board[i][j]) > 1 or \
                square.count(board[i][j]) > 1:
            return False
        return True



board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Solution().solve(board)
for i in board:
    print(i)
