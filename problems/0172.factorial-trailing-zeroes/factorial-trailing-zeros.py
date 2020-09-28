class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = n
        five_count = 0
        while temp:
            five_count += temp // 5
            temp //= 5
        return five_count



# 5! 120
print(Solution().trailingZeroes(20))