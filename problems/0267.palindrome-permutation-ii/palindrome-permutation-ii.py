from typing import List
import itertools
import copy

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        if sum([x%2 for x in d.values()]) > 1:
            return []
        half = ''
        mid = ''
        for c in d:
            half += c * (d[c] // 2)
            if d[c] % 2 == 1:
                mid = c
        res = self._generate_half({x: d[x]//2 for x in d if d[x]>=2})
        if not res and mid:
            return [mid]
        return [x + mid + x[::-1] for x in res]

    def _generate_half(self, char_dict):
        if not char_dict:
            return []
        res = []
        def dfs(s, char_dict):
            if not char_dict:
                res.append(s)
            else:
                for c in char_dict:
                    temp = copy.copy(char_dict)
                    if temp[c] == 1:
                        del temp[c]
                    else:
                        temp[c] -= 1
                    dfs(s+c, temp)
        dfs('', char_dict)
        return res

print(Solution().generatePalindromes("a"
))






# 示例 1：
#
# 输入: "aabb"
# 输出: ["abba", "baab"]
#
# 示例 2：
#
# 输入: "abc"
# 输出: []