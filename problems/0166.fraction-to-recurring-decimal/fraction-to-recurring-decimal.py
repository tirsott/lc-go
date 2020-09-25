import math

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        flag = False
        if numerator * denominator < 0:
            flag = True
        numerator, denominator = abs(numerator), abs(denominator)
        numerator, denominator = numerator//math.gcd(numerator, denominator), denominator//math.gcd(numerator, denominator)
        left = numerator // denominator
        right = numerator % denominator
        right_list = []
        right_dict = {}
        while right:
            if right not in right_dict:
                right_dict[right] = len(right_list)
            else:
                right_list.insert(right_dict[right], '(')
                right_list.append(')')
                break
            right *= 10
            while right < denominator:
                right *= 10
                right_list.append('0')
            right_list.append(str(right // denominator))
            right = right % denominator
        if right_list:
            right_list.insert(0, '.')
        return str(left) + ''.join(right_list) if not flag else '-' + str(left) + ''.join(right_list)



print(Solution().fractionToDecimal(-2, 3))


# 示例 2:
#
# 输入: numerator = 2, denominator = 1
# 输出: "2"
#
# 示例 3:
#
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
