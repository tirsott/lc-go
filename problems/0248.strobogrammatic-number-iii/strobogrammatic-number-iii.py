from typing import List

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        low_len = len(low)
        high_len = len(high)
        res = 0
        for i in range(low_len, high_len+1):
            nums = self.findStrobogrammatic(i)
            res += len([x for x in nums if int(low) <= int(x) <= int(high)])
        return res


    def findStrobogrammatic(self, n: int) -> List[str]:
        mapping = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        dp = [[] for _ in range(max(3, (n + 1)))]
        dp[0] = []
        dp[1] = ['1', '8', '0']
        if n == 1:
            return dp[1]
        dp[2] = ['11', '69', '88', '96', '00']

        for i in range(3, n + 1):
            for x in dp[i - 2]:
                for y in mapping.keys():
                    dp[i].append(y + x + mapping[y])
        return [x for x in dp[n] if not x.startswith('0')]


print(Solution().strobogrammaticInRange('50', '100'))