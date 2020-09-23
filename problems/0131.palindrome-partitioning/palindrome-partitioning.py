from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        def dfs(s, exist_strs):
            if not s:
                res.append(exist_strs)
            for i in range(len(s)):
                if self.is_palindrome(s[:i+1]):
                    dfs(s[i+1:], exist_strs+[s[:i+1]])
        dfs(s, [])
        return res

    def is_palindrome(self, s):
        return s == s[::-1]







# 'aab'
print(Solution().partition('aab'))