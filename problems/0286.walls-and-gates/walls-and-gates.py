from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        row = len(rooms)
        col = len(rooms[0])
        start = [[x, y] for x in range(row) for y in range(col) if rooms[x][y]==0]
        count = len(start)
        min = 0
        while start:
            temp = []
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for p in start:
                for d in directions:
                    if p[0] + d[0] in range(row) and p[1] + d[1] in \
                            range(col) and rooms[p[0] + d[0]][p[1] + d[1]] > min:
                        rooms[p[0] + d[0]][p[1] + d[1]] = min + 1
                        temp.append([p[0] + d[0], p[1] + d[1]])
                        count -= 1
            min += 1
            start = temp

a = [[2147483647, -1, 0, 2147483647], [2147483647,2147483647,2147483647,-1],
     [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
import time
t = time.time()
print(Solution().wallsAndGates(a))
print(time.time()-t)

# 给定二维网格：
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
#
# 运行完你的函数后，该网格应该变成：
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
#
