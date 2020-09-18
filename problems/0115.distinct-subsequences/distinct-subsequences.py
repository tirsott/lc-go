class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) <= len(t) or not t:
            return 1 if s == t else 0
        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
        for i in range(len(t)):
            dp[i][i] = 1 if s[:i+1] == t[:i+1] else 0
        for i in range(len(s)):
            dp[i][0] = s[:i+1].count(t[0])
        print(dp)
        for i in range(1, len(s)):
            for j in range(1, min(i, len(t))):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
            print(dp)
        return dp[len(s)-1][len(t)-1]


# S = "rabbbit" T = "rabbit"
print(Solution().numDistinct("babgbag", "bag"))