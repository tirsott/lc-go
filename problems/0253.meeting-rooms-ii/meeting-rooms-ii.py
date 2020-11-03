from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append([intervals[i]])
                continue
            flag = False
            for r in res:
                if intervals[i][0] >= r[-1][1]:
                    r.append(intervals[i])
                    flag = True
                    break
            if not flag:
                res.append([intervals[i]])
        return len(res)

print(Solution().minMeetingRooms([[7,10],[2,4]]))

# 示例 1:
#
# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
#
# 示例 2:
#
# 输入: [[7,10],[2,4]]
# 输出: 1