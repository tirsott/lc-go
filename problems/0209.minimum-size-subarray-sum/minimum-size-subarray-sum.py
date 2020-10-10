from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        res = 0
        left = 0
        right = 0
        while left < len(nums) - 1:
            while sum(nums[left:right+1]) < s and right < len(nums) - 1:
                right += 1
            if sum(nums[left:right+1]) < s:
                return res
            if res == 0:
                res = right - left + 1
            else:
                res = min(res, right-left+1)
            left += 1
        return res



# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
import time
t = time.time()
s = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(120331635, s[:100000]))
# print(Solution().minSubArrayLen(7, s[:100000]))
print(time.time()-t)
