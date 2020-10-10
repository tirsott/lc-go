class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
        return True



# 输入: s = "paper", t = "title"
# 输出: true
print(Solution().isIsomorphic(s = "ab", t = "aa"))