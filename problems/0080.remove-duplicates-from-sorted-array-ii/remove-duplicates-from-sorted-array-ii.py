from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        count = 0
        while p < len(nums) - 1:
            if nums[p+1] == nums[p] and count >=1:
                nums.pop(p+1)
            elif nums[p+1] == nums[p]:
                count += 1
                p += 1
            else:
                count = 0
                p += 1
        return len(nums)


print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))