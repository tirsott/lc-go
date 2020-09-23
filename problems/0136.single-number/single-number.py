from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res



# [4,1,2,1,2]
print(Solution().singleNumber([4,1,2,1,2]))