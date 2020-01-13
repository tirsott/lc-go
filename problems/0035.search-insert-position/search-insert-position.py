from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right - 1 and nums[left] != target and nums[right] != target:
                if target < nums[left]:
                    return left
                elif target > nums[right]:
                    return right + 1
                else:
                    return right
            if left == right and nums[left] != target:
                return left if target < nums[left] else left + 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if target < nums[left] else left + 1

for i in range(10):
    print(Solution().searchInsert([1], i))