class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        s = str(n)
        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                if int(s[i]) >= 1:
                    res += (1 + n // 10)
                else:
                    res += n // 10
            elif s[i] == '1':
                res += (int(s[i+1:]) + 1 + n // 10**(len(s)-i) * 10**(len(
                    s)-i-1))
            elif s[i] == '0':
                res += n // 10**(len(s)-i) * 10**(len(s)-i-1)
            else:
                res += (n // 10**(len(s)-i)+1) * 10**(len(s)-i-1)
        return res



# 示例:
#
# 输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
import time
t = time.time()
n = 824883
print(Solution().countDigitOne(113))
print(time.time()-t)