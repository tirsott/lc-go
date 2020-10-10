from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [0, nums[0]]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1])



# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
print(Solution().rob([2,1,1,2]))