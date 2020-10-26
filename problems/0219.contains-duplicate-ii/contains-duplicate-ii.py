from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                if i - d[nums[i]][-1] <= k:
                    return True
                else:
                    d[nums[i]].append(i)
        return False


# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
nums = [i for i in range(-24500, 30000)]
import time
t = time.time()
print(Solution().containsNearbyDuplicate(nums, 35000))
print(time.time()-t)