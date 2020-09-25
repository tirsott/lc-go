class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        if len(s) == len(t):
            for i in range(len(s)):
                if s[:i]+s[i+1:] == t[:i]+t[i+1:]:
                    return True
        if len(s) > len(t):
            t, s = s, t
        for i in range(len(t)):
            if s == t[:i]+t[i+1:]:
                return True
        return False


print(Solution().isOneEditDistance(s = "1203", t = "1213"))