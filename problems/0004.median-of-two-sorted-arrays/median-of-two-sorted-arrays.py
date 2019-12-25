from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while len(nums1) > 2 and len(nums2) > 2:
            if self.get_median(nums1) == self.get_median(nums2):
                return self.get_median(nums1)
            elif self.get_median(nums1) > self.get_median(nums2):
                cut = min(self.get_cut_len(nums1), self.get_cut_len(nums2))
                nums1 = nums1[:len(nums1)-cut]
                nums2 = nums2[cut:]
            else:
                cut = min(self.get_cut_len(nums1), self.get_cut_len(nums2))
                nums1 = nums1[cut:]
                nums2 = nums2[:len(nums2) - cut]
        return self.get_median(sorted(nums1+nums2))

    def get_median(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    def get_cut_len(self, nums):
        if len(nums) % 2 == 1:
            return len(nums) // 2
        else:
            return len(nums) // 2 - 1

if __name__ == '__main__':
    nums1 = [1, 2, 6, 7]
    nums2 = [3, 4, 5, 8]
    print(Solution().findMedianSortedArrays(nums1, nums2))