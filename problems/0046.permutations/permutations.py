from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, combine, target):
            if target == []:
                res.append(combine)
            else:
                for i in range(len(target)):
                    dfs(res, combine + [target[i]], target[:i]+target[i+1:])
        res = []
        dfs(res, [], nums)
        return res

print(Solution().permute([1,2,3]))