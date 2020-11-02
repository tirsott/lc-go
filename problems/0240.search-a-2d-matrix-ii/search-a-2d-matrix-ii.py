class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0])-1
        while 0 <= i <= len(matrix)-1 and 0 <= j <= len(matrix[0])-1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

print(Solution().searchMatrix([[1,4,7,11,15],
                               [2,5,8,12,19],
                               [3,6,9,16,22],
                               [10,13,14,17,24],
                               [18,21,23,26,30]]
,5))


# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
