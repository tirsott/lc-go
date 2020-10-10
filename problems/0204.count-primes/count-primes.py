import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = False
        is_prime[1] = False
        count = 0
        # for i in range(2, math.ceil(math.sqrt(n)) + 1):
        for i in range(2, n):
            if not is_prime[i]:
                continue
            count += 1
            for j in range(2 * i, n, i):
                is_prime[j] = False
        return count

import time
t = time.time()
print(Solution().countPrimes(1000000))
print(time.time() - t)