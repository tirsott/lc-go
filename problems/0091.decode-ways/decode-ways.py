
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1] + s[i]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]




print(Solution().numDecodings("10"
))