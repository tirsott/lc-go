class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return math.factorial(m+n-2) // (math.factorial(n-1) * math.factorial(m-1))

print(Solution().uniquePaths(7, 3))