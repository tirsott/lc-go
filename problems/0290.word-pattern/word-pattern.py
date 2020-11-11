class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d and s_list[i] != d[pattern[i]]:
                return False
            elif s_list[i] in d.values() and pattern[i] not in d:
                return False
            elif pattern[i] not in d:
                d[pattern[i]] = s_list[i]
        return True