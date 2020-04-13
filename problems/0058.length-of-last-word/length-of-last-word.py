class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        res = 0
        while right >= 0 and s[right] == ' ':
            right -= 1
        while right >= 0 and s[right] != ' ':
            res += 1
            right -= 1
        return res

print(Solution().lengthOfLastWord("Hello World"))