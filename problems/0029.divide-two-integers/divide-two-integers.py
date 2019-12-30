class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if (divisor < 0 and dividend > 0) or (divisor > 0 and
                                                       dividend < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            mi = 1
            temp = divisor
            while dividend >= divisor << 1:
                divisor <<= 1
                mi <<= 1
            dividend -= divisor
            res += mi
            divisor = temp
        if flag == 1:
            return min(res, 2147483647)
        else:
            return max(-res, -2147483648)