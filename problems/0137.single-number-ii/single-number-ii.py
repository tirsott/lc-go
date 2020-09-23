from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
        return ones


print(Solution().singleNumber( [2,2,3,2]))