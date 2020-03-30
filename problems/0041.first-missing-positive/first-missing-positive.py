from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return [x for x in range(1, len(nums) + 2) if x not in nums][0]