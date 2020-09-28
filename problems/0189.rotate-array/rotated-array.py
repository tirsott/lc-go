from typing import List
import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = self.rotate_nums(nums, k)

    def rotate_nums(self, nums, k):
        if k == 0:
            return nums
        for i in range(math.ceil(len(nums)/k)-1):
            for j in range(k):
                if (i+1) * k + j < len(nums):
                    nums[j], nums[(i+1) * k + j] = nums[(i+1) * k + j], nums[j]
        if len(nums)%k == 0:
            return nums
        else:
            return self.rotate_nums(nums[:k], k-len(nums)%k) + nums[k:]


# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# print(Solution().rotate_nums([1,2,3,4,5,6,7], 3))
n =  [1,2,3,4,5,6,7]
Solution().rotate(n, 3)
print(n)