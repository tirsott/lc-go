from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        count = 0
        last = len(nums) - 1
        while count <= last:
            if nums[count] == val:
                nums[count], nums[last] = nums[last], nums[count]
                last -= 1
                continue
            else:
                count += 1
        return count

if __name__ == '__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))