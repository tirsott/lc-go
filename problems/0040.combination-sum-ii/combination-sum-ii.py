from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, start, path, target, res):
            if target == 0 and sorted(path) not in res:
                res.append(sorted(path))
            else:
                for i in range(start, len(candidates)):
                    if target < 0:
                        break
                    dfs(candidates, i+1, path + [candidates[i]], target -
                        candidates[i], res)
        path = []
        res = []
        dfs(candidates, 0, path, target, res)
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))