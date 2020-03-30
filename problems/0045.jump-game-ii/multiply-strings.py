from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        cnt = 0
        last = 0
        for i in range(len(nums)):
            if i > cur:
                return
            if i > last:
                last = cur
                cnt += 1
            cur = max(cur, i + nums[i])
        return cnt

print(Solution().jump([2,3,0,1,4]))