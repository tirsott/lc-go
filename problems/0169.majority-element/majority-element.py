from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            if d[nums[i]] == (len(nums) + 1) // 2:
                return nums[i]


print(Solution().majorityElement([2,2,1,1,1,2,2]))
