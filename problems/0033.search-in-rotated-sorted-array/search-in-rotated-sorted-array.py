from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return nums.index(target) if target in nums else -1
        min_index = self.get_min_index(nums)
        new_nums = nums[min_index:] + nums[:min_index]
        left = 0
        res = -1
        right = len(new_nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if new_nums[mid] == target:
                res = mid
                break
            elif new_nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if res in range(len(nums) - min_index, len(nums)):
            return res - (len(nums) - min_index)
        elif res in range(len(nums) - min_index):
            return res + min_index
        else:
            return res


    def get_min_index(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

for i in [0,1,2,4,5,6,7]:
    print(Solution().search([4,5,6,7,0,1,2], i))