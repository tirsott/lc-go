class Solution:
    def myAtoi(self, str: str) -> int:
        tem = ''
        i = 1
        str = str.lstrip()
        l = len(str)
        if not str:
            return 0
        if str[0] in '+-' or str[0] in '0123456789':
            tem += str[0]
            while i < l:
                if str[i] in '0123456789':
                    tem += str[i]
                    i += 1
                else:
                    break
        if not tem or tem == '+' or tem == '-':
            return 0
        tem = int(tem)
        if tem < -2147483648:
            return -2147483648
        elif tem > 2147483647:
            return 2147483647
        else:
            return tem