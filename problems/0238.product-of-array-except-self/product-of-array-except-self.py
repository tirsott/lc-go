from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = reduce(lambda x, y: x*y, nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(reduce(lambda x, y: x*y, nums[:i]+nums[i+1:]))
            else:
                res.append(product//nums[i])
        return res

# 输入: [1,2,3,4]
# 输出: [24,12,8,6]