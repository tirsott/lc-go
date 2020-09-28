class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[-1]) - 64) * (26 ** i)
            s = s[:-1]
        return res



print(Solution().titleToNumber("ZY"))