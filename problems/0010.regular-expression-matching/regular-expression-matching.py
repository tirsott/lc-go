import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        print(i, j)
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] | dp[i+1][j] | dp[i][j+1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    print(Solution().isMatch('aab', 'c*a*b'))