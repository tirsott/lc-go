from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(s, wordDict, exist_word):
            if not self.exist(s, wordDict):
                return
            if not s:
                res.append(' '.join(exist_word))
            for word in wordDict:
                if s.startswith(word):
                    dfs(s[len(word):], wordDict, exist_word + [word])
        dfs(s, wordDict, [])
        return res

    def exist(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]



# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa",
  "aaaaaaaaaa"]
))