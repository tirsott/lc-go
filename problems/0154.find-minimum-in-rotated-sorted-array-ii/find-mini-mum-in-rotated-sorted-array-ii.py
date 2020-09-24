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
            elif nums[mid-1] > nums[-1]:
                return self.findMin(nums[mid:])
            else:
                return self.findMin(nums[:-1])


import time
t = time.time()
print(Solution().findMin([3,3,3,3,3,3,3,3,1,3]))
print(time.time()-t)