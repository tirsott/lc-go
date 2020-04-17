class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s.strip())
            return True
        except:
            return False

print(Solution().isNumber(" 1e"))