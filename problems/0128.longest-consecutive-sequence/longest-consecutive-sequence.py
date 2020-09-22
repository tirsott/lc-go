from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for num in nums:
            if num not in d:
                left = d.get(num-1, 0)
                right = d.get(num+1, 0)
                d[num] = 1 + left + right
                res = max(res, d[num])
                d[num-left] = d[num]
                d[num+right] = d[num]
        return res




# [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))