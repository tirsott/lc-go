from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(exist_nums, left_nums, res):
            if  exist_nums not in res:
                res.append(exist_nums)
            for num in left_nums:
                dfs(exist_nums+[num], left_nums[left_nums.index(num)+1:], res)
        dfs([], nums, res)
        return res

print(Solution().subsets([1,2,3]))