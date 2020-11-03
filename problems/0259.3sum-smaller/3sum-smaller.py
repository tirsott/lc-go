from typing import List
import itertools

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        # for t in list(itertools.combinations(nums, 3)):
        #     if sum(t) < target:
        #         res += 1
        # return res
        for i in range(len(nums)-2):
            if nums[i] >= target and nums[i] >= 0:
                return res
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[j] >= target and nums[j] >= 0:
                    break
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] < target:
                        res += 1
                    elif nums[k] >= 0:
                        break
        return res

import time
t = time.time()
print(Solution().threeSumSmaller(nums = [-2, -1, 0, 1, 2, 3], target = 2))
print(time.time()-t)



# 示例：
#
# 输入: nums = [-2,0,1,3], target = 2
# 输出: 2
# 解释: 因为一共有两个三元组满足累加和小于 2:
#      [-2,0,1]
#      [-2,0,3]
#
