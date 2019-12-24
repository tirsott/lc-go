class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_length = 1
        len_list = [1] * len(s)
        last_position = {s[0]: 0}
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                len_list[i] = 1
                last_position[s[i]] = i
                continue
            # if s[i] not in s[i-len_list[i-1]:i]:
            if s[i] not in last_position or last_position[s[i]] < i - len_list[i-1]:
                len_list[i] = len_list[i - 1] + 1
                last_position[s[i]] = i
                max_length = max(max_length, len_list[i])
            else:
                len_list[i] = i - last_position[s[i]]
                max_length = max(max_length, len_list[i])
                last_position[s[i]] = i
            print(len_list, last_position, max_length)
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))