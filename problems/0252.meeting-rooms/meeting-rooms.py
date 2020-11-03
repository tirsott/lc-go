from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

print(Solution().canAttendMeetings([[7,10],[2,4]]))


# 示例 1:
#
# 输入: [[0,30],[5,10],[15,20]]
# 输出: false
#
# 示例 2:
#
# 输入: [[7,10],[2,4]]
# 输出: true
#
