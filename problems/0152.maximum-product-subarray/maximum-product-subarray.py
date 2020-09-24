from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], 0] if nums[0] > 0 else [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                if dp[i-1][0] <=0:
                    dp[i][0] = nums[i]
                else:
                    dp[i][0] = dp[i-1][0] * nums[i]
                if dp[i-1][1] < 0:
                    dp[i][1] = dp[i-1][1] * nums[i]
                else:
                    dp[i][1] = 0
            else:
                if dp[i-1][0] <=0:
                    dp[i][1] = nums[i]
                else:
                    dp[i][1] = dp[i-1][0] * nums[i]
                if dp[i-1][1] < 0:
                    dp[i][0] = dp[i-1][1] * nums[i]
                else:
                    dp[i][0] = 0
        return max([x[0] for x in dp])



# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
print(Solution().maxProduct([-2]))