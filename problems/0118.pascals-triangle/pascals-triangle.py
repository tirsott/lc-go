from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                line = [1]
            else:
                line = [1 for _ in range(i+1)]
                for j in range(1, i):
                    line[j] = res[i-1][j] + res[i-1][j-1]
            res.append(line)
        return res

print(Solution().generate(5))