class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        return x == self.reverse(x)



    def reverse(self, x: int) -> int:
        if x < 0:
            x = - x
            flag = -1
        else:
            flag = 1
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return res * flag if res * flag in range(-2 ** 31, 2 ** 31 - 1) else 0

if __name__ == '__main__':
    print(Solution().reverse(0))