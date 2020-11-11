import copy

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        if not pattern or not s:
            return pattern == s
        def dfs(pattern, s, d):
            if pattern and not s:
                return False
            if len(pattern) == 1:
                if (s not in d.values() and pattern[0] not in d) or\
                        (pattern[0] in d and d[pattern[0]] == s):
                    return True
            else:
                if pattern[0] in d:
                    if s.startswith(d[pattern[0]]):
                        return dfs(pattern[1:], s[len(d[pattern[0]]):], d)
                    else:
                        return False
                else:
                    for i in range(1, len(s)):
                        if s[:i] in d.values():
                            continue
                        temp = copy.copy(d)
                        temp.update({pattern[0]: s[:i]})
                        if dfs(pattern[1:], s[i:], temp):
                            return True
            return False
        return dfs(pattern, s, {})

print(Solution().wordPatternMatch(pattern = "ab", s = "aa"))



# 示例 1：
#
# 输入：pattern = "abab", s = "redblueredblue"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "red"
# 'b' -> "blue"
#
# 示例 2：
#
# 输入：pattern = "aaaa", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "asd"
#
# 示例 3：
#
# 输入：pattern = "abab", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "a"
# 'b' -> "sdasd"
# 注意 'a' 和 'b' 不能同时映射到 "asd"，因为这里的映射是一种双射。
#
# 示例 4：
#
# 输入：pattern = "aabb", s = "xyzabcxzyabc"
# 输出：false
