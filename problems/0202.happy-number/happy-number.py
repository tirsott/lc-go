class Solution:
    def isHappy(self, n: int) -> bool:
        exist = []
        while 1:
            if n == 1:
                return True
            if n in exist:
                return False
            exist.append(n)
            n = self.square_sum(n)


    def square_sum(self, n):
        res = 0
        while n > 0:
            res += (n%10) ** 2
            n //= 10
        return res

print(Solution().isHappy(2))