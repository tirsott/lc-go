from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.find(nums, 0, len(nums)-1)



    def find(self, nums, start, end):
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
        return start


# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
print(Solution().findPeakElement([1,2]))