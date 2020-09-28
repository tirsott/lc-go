from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == nums[-1] == '0':
            nums = nums[:1]
        return ''.join(nums[::-1])


# 输入: [3,30,34,5,9]
# 输出: 9534330
print(Solution().largestNumber([0, 0]))