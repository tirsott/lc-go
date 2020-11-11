from typing import List
from itertools import combinations
import copy

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        while s.startswith(')'):
            s = s[1:]
        while s.endswith('('):
            s = s[:-1]
        if not s:
            return [""]
        s_list = list(s)
        res = []
        left = [i for i in range(len(s)) if s[i] == '(']
        right = [i for i in range(len(s)) if s[i] == ')']
        count = 0
        min_right = 0
        for i in left:
            for j in range(max(i+1, min_right), len(s)):
                if s[j] == ')':
                    count += 1
                    min_right = j + 1
                    break
        left_comb = list(combinations(left, count))
        right_comb = list(combinations(right, count))
        for l in left_comb:
            for r in right_comb:
                if [i for i in range(count) if l[i] > r[i]]:
                    continue
                else:
                    temp = copy.copy(s_list)
                    for x in [i for i in left if i not in l]:
                        temp[x] = ''
                    for x in [i for i in right if i not in r]:
                        temp[x] = ''
                    if ''.join(temp) not in res:
                        res.append(''.join(temp))
        return res


print(Solution().removeInvalidParentheses("(()"))

# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
#  1 0 1 0 -1 0 -1
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
#
# 示例 3:
#
# 输入: ")("
# 输出: [""]
# -1 0
