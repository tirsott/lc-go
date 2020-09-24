class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # if len(s) < 3:
        #     return len(s)
        # dp = [[[None, None], [None, None]] for _ in range(len(s))]
        # dp[0] = [[s[0], 1], [s[0], 1]]
        # res = 0
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         dp[i] = [[s[i], dp[i-1][0][1]+1], [dp[i-1][1][0], dp[i-1][1][1]+1]]
        #         res = max(res, dp[i][0][1], dp[i][1][1])
        #     else:
        #         dp[i][0] = [s[i], 1]
        #         if s[i] in dp[i-1][1][0]:
        #             dp[i][1] = [dp[i-1][1][0], dp[i-1][1][1]+1]
        #         else:
        #             dp[i][1] = [s[i]+s[i-1], dp[i-1][0][1]+1]
        #         res = max(res, dp[i][0][1], dp[i][1][1])
        # return res
        if len(s) < 3:
            return len(s)
        res = 1
        count = [[s[0], 1], ['', 0]]
        for i in range(1, len(s)):
            if not count[1][0]:
                if s[i] == count[0][0]:
                    count[0][1] += 1
                else:
                    count[1][0] = s[i]
                    count[1][1] = 1
            else:
                if s[i] == count[1][0]:
                    count[1][1] += 1
                elif s[i] == count[0][0]:
                    count[0] = [count[1][0], count[0][1]+count[1][1]]
                    count[1] = [s[i], 1]
                else:
                    count[0] = count[1]
                    count[1] = [s[i], 1]
            res = max(res, count[0][1]+count[1][1])
        return res


# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))