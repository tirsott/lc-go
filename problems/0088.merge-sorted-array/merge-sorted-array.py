from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = 0, 0
        while index2 < n:
            while index1 < m + index2 and nums1[index1] <= nums2[index2]:
                index1 += 1
            nums1.insert(index1, nums2[index2])
            index2 += 1
        for i in range(n):
            nums1.pop()



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)