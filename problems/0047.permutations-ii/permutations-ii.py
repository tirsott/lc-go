from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, combine, target):
            if target == [] and combine not in res:
                res.append(combine)
            else:
                for i in range(len(target)):
                    dfs(res, combine + [target[i]], target[:i]+target[i+1:])
        res = []
        dfs(res, [], nums)
        return res

print(Solution().permuteUnique([1,1,2]))