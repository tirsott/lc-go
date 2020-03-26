from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        def dfs(candidates, path, start, target, res):
            if target == 0:

                res.append(path)
            else:
                for i in range(start, len(candidates)):
                    if target < 0:
                        break
                    dfs(candidates, path + [candidates[i]], i,
                        target - candidates[i], res)

        res = []
        dfs(candidates, [], 0, target, res)
        return res