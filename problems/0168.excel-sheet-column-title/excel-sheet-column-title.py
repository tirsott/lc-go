class Solution:
    def convertToTitle(self, n: int) -> str:
        str = ''
        while n:
            if n % 26 == 0:
                str = 'Z' + str
                n -= 26
                n //= 26
            else:
                str = chr(64 + n % 26) + str
                n = n // 26
        return str


print(Solution().convertToTitle(260))