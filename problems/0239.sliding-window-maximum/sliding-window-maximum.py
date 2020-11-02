from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        res.append(max(nums[:k]))
        for i in range(k, len(nums)):
            if nums[i] >= res[-1]:
                res.append(nums[i])
            else:
                if nums[i-k] == res[-1]:
                    res.append(max(nums[i+1-k:i+1]))
                else:
                    res.append(res[-1])
        return res


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))



# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
