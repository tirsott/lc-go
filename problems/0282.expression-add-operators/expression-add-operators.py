from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(prefix, num, last, total):
            if total == target and not num:
                res.append(prefix)
            elif not num:
                return
            else:
                for i in range(len(num)):
                    if num.startswith('0') and i > 0:
                        continue
                    if not prefix:
                        dfs(num[:i+1], num[i+1:], int(num[:i+1]), int(num[:i+1]))
                    else:
                        dfs(prefix + '+' + num[:i + 1], num[i + 1:], int(num[:i+ 1]),
                            total + int(num[:i + 1]))
                        dfs(prefix + '-' + num[:i + 1], num[i + 1:],
                            -int(num[:i+ 1]), total - int(num[:i + 1]))
                        dfs(prefix + '*' + num[:i + 1], num[i + 1:],
                            (int(num[:i+1]))*last, total + (int(num[:i+1])-1)*last)
        dfs('', num, 0, 0)
        return res

print(Solution().addOperators(num = "3456237490", target = 9191))


# 示例 1:
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
#
# 示例 2:
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
#
# 示例 3:
#
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
#
# 示例 4:
#
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
#
# 示例 5:
#
# 输入: num = "3456237490", target = 9191
# 输出: []
