from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        return max([nums[i+1] - nums[i] for i in range(len(
            nums)-1)])




# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
import time
t = time.time()
print(Solution().maximumGap([3,6,9,1]))
print(time.time()-t)