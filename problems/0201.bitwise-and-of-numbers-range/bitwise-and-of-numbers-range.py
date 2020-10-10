class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        offset = 0
        while m != n:
            m >>= 1
            n >>= 1
            offset += 1
        return m << offset

import time
t = time.time()
print(Solution().rangeBitwiseAnd(0, 214748364))
print(time.time() - t)