from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        left = 0
        while left < len(intervals):
            if left == 0:
                left += 1
                continue
            if intervals[left][0] <= intervals[left - 1][1]:
                intervals[left - 1] = [intervals[left - 1][0],
                                       max(intervals[left - 1][1],
                                           intervals[left][1])]
                intervals.pop(left)
            else:
                left += 1
        return intervals

print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))