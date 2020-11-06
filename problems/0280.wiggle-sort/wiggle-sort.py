from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(len(nums) // 2):
            nums.insert(i*2+1, nums.pop())

print(Solution().wiggleSort([3,5,2,1,6,4]))




# 示例:
#
# 输入: nums = [3,5,2,1,6,4]
# 输出: 一个可能的解答是 [3,5,1,6,2,4]