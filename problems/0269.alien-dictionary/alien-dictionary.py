from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d = {}
        for word in words:
            for c in word:
                if c not in d:
                    d[c] = []

        def _get_order(words):
            nonlocal d
            words = [word for word in words if word]
            if len(words) == 1:
                if words[0][0] not in d:
                    d[words[0][0]] = []
            for i in range(0, len(words)):
                if i == 0:
                    if words[0][0] not in d:
                        d[words[0][0]] = []
                    continue
                if words[i][0] != words[i-1][0]:
                    if words[i][0] in d and words[i-1][0] not in d[words[i][0]]:
                        d[words[i][0]].append(words[i-1][0])
                    else:
                        d[words[i][0]] = [words[i-1][0]]
            same_prefix = self._get_same_prefix(words)
            while same_prefix:
                temp = []
                for word_list in same_prefix:
                    if '' in word_list and word_list.index('') > 0:
                        d = {}
                        return
                    _get_order(word_list)
                    temp += self._get_same_prefix(word_list)
                same_prefix = temp
        _get_order(words)
        res = ''
        while d:
            temp1 = res
            for k in d:
                if not d[k]:
                    res += k
                    del d[k]
                    break
            if temp1 == res:
                return ''
            else:
                for k in d:
                    if res[-1] in d[k]:
                        d[k].remove(res[-1])
        return res

    def _get_same_prefix(self, words):
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][:k] == words[j][:k]:
                        res.append([words[i][k:], words[j][k:]])
                        break
        return res


print(Solution().alienOrder(["abc","ab"]
))

# 示例 1：
#
# 输入:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# 输出: "wertf"
#          w [[], [rtf]]
# 示例 2：
#
# 输入:
# [
#   "z",
#   "x"
# ]
# 输出: "zx"
#
# 示例 3：
#
# 输入:
# [
#   "z",
#   "x",
#   "z"
# ]
# 输出: ""
# 解释: 此顺序是非法的，因此返回 ""
