from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        intervals = []
        i = 0
        while i < len(nums):
            start = i
            while i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
                i += 1
            if start == i:
                intervals.append(str(nums[i]))
            else:
                intervals.append(f'{nums[start]}->{nums[i]}')
            i += 1
        return intervals


print(Solution().summaryRanges([-1]))

# 示例 1：
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
# 示例 2：
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
# 示例 3：
#
# 输入：nums = []
# 输出：[]
#
# 示例 4：
#
# 输入：nums = [-1]
# 输出：["-1"]
#
# 示例 5：
#
# 输入：nums = [0]
# 输出：["0"]
