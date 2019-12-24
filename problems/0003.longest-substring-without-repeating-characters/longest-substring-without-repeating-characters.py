class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1 if s else 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    max_length = max(max_length, j - i + 1)
                else:
                    break
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))