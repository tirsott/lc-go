from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        res = []


        def dfs(exist_num, left_num, count, res):
            if count == 1:
                for num in left_num:
                    res.append(exist_num + [num])
            else:
                for num in left_num:
                    dfs(exist_num+[num], left_num[left_num.index(num)+1:],
                        count-1, res)
        dfs([], nums, k, res)
        return res

print(Solution().combine(4, 2))