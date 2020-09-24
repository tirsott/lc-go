from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        mid = (len(nums) + 1) // 2
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        else:
            if nums[mid-1] < nums[-1]:
                return self.findMin(nums[:mid])
            else:
                return self.findMin(nums[mid:])



# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 12345
# 23451
# 34512
# 45123
# 51234

import time
t = time.time()
print(Solution().findMin([2,2,2,0,1]))
print(time.time()-t)
