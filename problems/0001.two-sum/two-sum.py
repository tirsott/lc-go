from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in pos_dict:
                pos_dict[nums[i]] = i
            else:
                return [pos_dict[target - nums[i]], i]

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))