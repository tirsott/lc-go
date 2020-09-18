from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = []
        for i in range(rowIndex+1):
            if i == 0:
                line = [1]
                last = line
            else:
                line = [1 for _ in range(i + 1)]
                for j in range(1, i):
                    line[j] = last[j] + last[j - 1]
                last = line
        return line

print(Solution().getRow(5))