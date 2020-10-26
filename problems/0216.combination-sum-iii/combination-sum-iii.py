from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs_comb(nums, exist_nums, target):
            if len(exist_nums) >= k:
                if sum(exist_nums) == n:
                    res.append(exist_nums)
            else:
                for i in range(len(nums)):
                    dfs_comb(nums[i+1:], exist_nums+[nums[i]], target-nums[i])
        dfs_comb([i for i in range(1, 10)], [], n)
        return res



# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
print(Solution().combinationSum3(2, 9))