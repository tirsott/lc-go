class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        dp = [i for i in range(len(s))]
        for i in range(1, len(s)):
            if self.is_palindrome(s[:i+1]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.is_palindrome(s[j:i+1]):
                    if j == 0:
                        dp[i] = 0
                        break
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
                else:
                    dp[i] = min(dp[i], dp[i-1] + 1)
        return dp[-1]

    def is_palindrome(self, s):
        return s == s[::-1]

import time
t = time.time()
print(Solution().minCut("ababababababababababababcbabababababababababababa"
))
print(time.time()-t)