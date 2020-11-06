from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        count = 0
        while i < l - count:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                count += 1
            else:
                i += 1
