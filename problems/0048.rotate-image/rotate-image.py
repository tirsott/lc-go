from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        123
        456
        789
        '''
        length = len(matrix[0])
        for i in range(length):
            for j in range(length//2):
                matrix[i][j], matrix[i][length-j-1] = matrix[i][length-j-1], matrix[i][j]
        for i in range(length):
            for j in range(length-i-1):
                matrix[i][j], matrix[length-j-1][length-i-1] = matrix[length-j-1][length-i-1], matrix[i][j]
        return