class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            dp[0][i] = dp[0][i-1] and s1[i-1] == s3[i-1]
            if not dp[0][i]:
                break
        for j in range(1, len(s2) + 1):
            dp[j][0] = dp[j-1][0] and s2[j-1] == s3[j-1]
            if not dp[j][0]:
                break
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s1[j-1] == s3[i+j-1])
        return dp[-1][-1]




# s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
s1= "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2= \
    "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3= \
    "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))