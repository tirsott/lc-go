from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not self.check_row(i, j, board) or not \
                            self.check_coloum(i, j, board) or not \
                            self.check_square(i, j, board):
                        return False
        return True

    def check_row(self, row, coloum, board):
        for j in range(coloum+1, 9):
            if board[row][j] == board[row][coloum]:
                return False
        return True

    def check_coloum(self, row, coloum, board):
        for i in range(row+1, 9):
            if board[i][coloum] == board[row][coloum]:
                return False
        return True

    def check_square(self, row, coloum, board):
        for i in range(row//3 * 3, row//3 * 3 + 3):
            for j in range(coloum // 3 * 3, coloum // 3 * 3 + 3):
                if board[i][j] == board[row][coloum] and not (i == row and j
                                                              == coloum):
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
print(Solution().isValidSudoku(board))