from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        position = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[position - 1]:
                nums[position] = nums[i]
                position += 1
        return position

print(Solution().removeDuplicates([1,1,3,3,4]))