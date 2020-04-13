from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        left = 0
        while left < len(intervals):
            if left == 0:
                left += 1
                continue
            if intervals[left][0] <= intervals[left-1][1]:
                intervals[left-1] = [intervals[left-1][0], max(intervals[left-1][1], intervals[left][1])]
                intervals.pop(left)
            else:
                left += 1
        return intervals

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))