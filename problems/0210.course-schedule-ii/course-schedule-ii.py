from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjcency = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        res = []
        for p in prerequisites:
            indegree[p[0]] += 1
            adjcency[p[1]].append(p[0])
        can_learn = [i for i in range(numCourses) if indegree[i]==0]
        while can_learn:
            temp = []
            res = res + can_learn
            for can in can_learn:
                for adj in adjcency[can]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        temp.append(adj)
            can_learn = temp
        return res if len(res) == numCourses else []


# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
#
# 示例 2:
#
# 输入: 4, [[1,0],[2,0],[3,1],[3,2]]
# 输出: [0,1,2,3] or [0,2,1,3]
# 解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
#      因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
#
import time
t = time.time()
s = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(4, s))
print(time.time()-t)