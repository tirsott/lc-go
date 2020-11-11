from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        need_modify = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.need_to_modify(board, i, j):
                    need_modify.append([i, j])
        for n_m in need_modify:
            board[n_m[0]][n_m[1]] = (board[n_m[0]][n_m[1]] + 1) % 2


    def need_to_modify(self, board, i, j):
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1],
                      [-1,-1]]
        count = [0, 0]
        for d in directions:
            if i+d[0] in range(len(board)) and j+d[1] in range(len(board[0])):
                count[board[i+d[0]][j+d[1]]] += 1
        if board[i][j] == 1:
            if count[1] < 2 or count[1] > 3:
                return True
            else:
                return False
        else:
            return count[1] == 3



# 示例：
#
# 输入：
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# 输出：
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
