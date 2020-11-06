from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return num



# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3