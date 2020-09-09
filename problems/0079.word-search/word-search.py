from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mark = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.backtrace(i, j, mark, board, word[1:]):
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def check_point(self, board, i, j, mark):
        return i in range(len(board)) and j in range(len(board[0])) and mark[
            i][j] != 1

    def backtrace(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direct in directs:
            x = i + direct[0]
            y = j + direct[1]
            if self.check_point(board, x, y, mark) and board[x][y] == word[0]:
                mark[x][y] = 1
                if self.backtrace(x, y, mark, board, word[1:]):
                    return True
                else:
                    mark[x][y] = 0
        return False


print(Solution().exist(
[["C","A","A"],
 ["A","A","A"],
 ["B","C","D"]],
"AAB"
))