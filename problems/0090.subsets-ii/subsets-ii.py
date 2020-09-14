from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(exist_nums, left_nums, res):
            if sorted(exist_nums) not in res:
                res.append(sorted(exist_nums))
            for j in range(len(left_nums)):
                dfs(exist_nums + [left_nums[j]], left_nums[j+1:], res)
        dfs([], nums, res)
        return res

print(Solution().subsetsWithDup([1,2,3,4,5,6,7,8,9,0]))