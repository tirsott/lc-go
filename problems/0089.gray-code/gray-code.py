from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        s = ['0', '1']
        for i in range(2, n+1):
            s = ['0' + x for x in s] + ['1' + x for x in s[::-1]]
        return [int('0b' + code, 2) for code in s]

print(Solution().grayCode(3))