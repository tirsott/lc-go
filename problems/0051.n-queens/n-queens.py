from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        l = [['Q' for _ in range(n)] for _ in range(n)]
        def dfs(row, puzzle):
            if row == n:
                res.append(puzzle)
                return
            if 'Q' not in puzzle[row]:
                return
            for i in range(n):
                if puzzle[row][i] == 'Q':
                    dfs(row+1, process_puzzle(puzzle, row, i))

        def process_puzzle(puzzle, row, i):
            p = copy.deepcopy(puzzle)
            for j in range(row+1, n):
                p[j][i] = '.'
            for j in range(n):
                if j != i:
                    p[row][j] = '.'
            for j in range(min(i, n-1-row)):
                p[row+j+1][i-j-1] = '.'
            for j in range(min(n-1-i, n-1-row)):
                p[row+j+1][i+j+1] = '.'
            return p
        dfs(0, l)

        return [[''.join(l) for l in ans] for ans in res]

print(Solution().solveNQueens(4))