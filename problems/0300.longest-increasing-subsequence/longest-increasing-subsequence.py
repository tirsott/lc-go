from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            index = len(nums) - i - 1
            flag = False
            for j in range(index+1, len(nums)):
                if nums[j] > nums[index]:
                    dp[index] = max(dp[index], dp[j] + 1)
                    flag = True
            if not flag:
                dp[index] = 1
        return max(dp) if dp else 0

print(Solution().lengthOfLIS([10,9,2,5,3,4]))

# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。