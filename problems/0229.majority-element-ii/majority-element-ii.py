from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [x for x in set(nums) if nums.count(x) > (len(nums)//3)]




# 示例 1：
#
# 输入：[3,2,3]
# 输出：[3]
#
# 示例 2：
#
# 输入：nums = [1]
# 输出：[1]
#
# 示例 3：
#
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
