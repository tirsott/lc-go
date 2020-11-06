class Solution:
    def __init__(self):
        self.mapping1 = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
            7: 'Seven', 8: 'Eight', 9: 'Nine', 0: ''
        }
        self.mapping2 = {
            1: 'One', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy', 8: 'Eighty', 9: 'Ninety', 0: 'And'
        }
        self.mapping11 = {
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 10: 'Ten'
        }


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        mapping = {
            0: '',
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }
        flag = 0
        res = []
        while num:
            if num % 1000:
                if flag:
                    res = self.number2words3(num%1000) + [mapping[flag]] + res
                else:
                    res = self.number2words3(num % 1000) + res
            num //= 1000
            flag += 1
        return ' '.join(res)


    def number2words3(self, num):
        res = []
        if num // 100 > 0:
            res.extend([self.mapping1[num // 100], 'Hundred'])
        num %= 100
        if not num:
            return res
        if num // 10 == 0:
            if res:
                res.extend([self.mapping1[num % 10]])
            else:
                res.extend([self.mapping1[num % 10]])
        elif num // 10 == 1:
            res.extend([self.mapping11[num]])
        else:
            if num%10 >0:
                res.extend([self.mapping2[num//10], self.mapping1[num%10]])
            else:
                res.extend([self.mapping2[num // 10]])
        return res

print(Solution().numberToWords(1000000
))
# 示例 1：
#
# 输入：num = 123
# 输出："One Hundred Twenty Three"
#
# 示例 2：
#
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
#
# 示例 3：
#
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# 示例 4：
#
# 输入：num = 1234567891
# 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
