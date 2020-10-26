from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        length = len(nums)
        for i in range(length):
            if len(res) < k:
                heapq.heappush(res, nums[i])
            elif nums[i] > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, nums[i])
        return heapq.heappop(res)



# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
import time, random
t = time.time()
print(Solution().findKthLargest([random.randint(0, 1000000) for _ in range(
    1000000)] , 4))
print(time.time()-t)