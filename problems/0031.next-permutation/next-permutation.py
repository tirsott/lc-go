from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        position = len(nums) - 1
        while position and nums[position] <= nums[position - 1]:
            position -= 1
        if position == 0:
            nums.reverse()
            return
        else:
            temp = nums.copy()
            for i in range(position, len(nums)):
                nums[i] = temp[position + len(nums) - i - 1]
        for i in range(position, len(nums)):
            if nums[i] > nums[position - 1]:
                nums[i], nums[position - 1] = nums[position - 1], \
                                                     nums[i]
                return

if __name__ == '__main__':
    nums  = [5,1,1]
    Solution().nextPermutation(nums)
    print(nums)