class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l <= 1:
            return s
        start, maxlen, i = 0, 1, 0
        while i < l:
            if l - i <= maxlen / 2:
                break
            left, right = i, i
            while right < l - 1 and s[right] == s[right + 1]:
                right += 1
            i = right + 1
            while right < l - 1 and left and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1
            if right - left + 1 > maxlen:
                maxlen = right - left + 1
                start = left
        return s[start:start + maxlen]

if __name__ == '__main__':
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('ab'))