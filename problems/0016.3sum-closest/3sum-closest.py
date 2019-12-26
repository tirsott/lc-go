from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums.sort()
        res = 2 ** 31
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                nsum = nums[i] + nums[left] + nums[right]
                if nsum == target:
                    return target
                elif abs(nsum - target) < abs(res - target):
                    res = nsum
                if nsum - target < 0:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,2,1,-4], 1))