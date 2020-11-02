class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        for i in range(len(num)//2+1):
            if num[-i-1] != mapping.get(num[i]):
                return False
        return True


print(Solution().isStrobogrammatic('2'))