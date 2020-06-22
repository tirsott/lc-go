from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return target in matrix[i]
        return False

print(Solution().searchMatrix(matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],
target = 13))

