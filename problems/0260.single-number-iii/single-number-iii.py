from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        exists = []
        for num in nums:
            if num not in exists:
                exists.append(num)
            else:
                exists.remove(num)
        return exists








# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]