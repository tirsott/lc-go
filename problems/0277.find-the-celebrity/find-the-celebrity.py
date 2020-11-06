# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
    return graph[a][b] == 1

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            flag = True
            for j in range(n):
                if not knows(j, i):
                    flag = False
                    break
            if flag:
                for j in range(n):
                    if i != j and knows(i, j):
                        return -1
                return i
        return -1



print(Solution().findCelebrity(3))

# 输入: graph = [
#   [1,1,0],
#   [0,1,0],
#   [1,1,1]
# ]
# 输出: 1
# 解释: 有编号分别为 0、1 和 2 的三个人。graph[i][j] = 1 代表编号为 i 的人认识编号为 j 的人，而 graph[i][j] = 0 则代表编号为 i 的人不认识编号为 j 的人。“名人” 是编号 1 的人，因为 0 和 2 均认识他/她，但 1 不认识任何人。
#
# 输入: graph = [
#   [1,0,1],
#   [1,1,0],
#   [0,1,1]
# ]
# 输出: -1
# 解释: 没有 “名人”