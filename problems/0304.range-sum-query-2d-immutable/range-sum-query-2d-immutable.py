from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cache = {}

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if (row1, col1, row2, col2) in self.cache:
            return self.cache[(row1, col1, row2, col2)]
        else:
            s = sum([sum([self.matrix[row][col] for col in range(col1, col2+1)])
                     for row in range(row1, row2+1)])
            self.cache[(row1, col1, row2, col2)] = s
            return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)