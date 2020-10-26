from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [[[0, 0], [0, 0]] for _ in range(len(nums))]
        dp[0] = [[nums[0], nums[0]], [0, 0]]
        dp[1] = [[nums[0], nums[0]], [nums[1], 0]]
        for i in range(2, len(nums) - 1):
            dp[i][0][0] = nums[i] + dp[i-1][0][1]
            dp[i][0][1] = max(dp[i-1][0][0], dp[i-1][0][1])
            dp[i][1][0] = nums[i] + dp[i-1][1][1]
            dp[i][1][1] = max(dp[i-1][1][0], dp[i-1][1][1])
        return max([dp[-2][0][0], dp[-2][0][1], dp[-2][1][0], dp[-2][1][1] +
                    nums[-1]])



# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
#
print(Solution().rob([2,3,2]))