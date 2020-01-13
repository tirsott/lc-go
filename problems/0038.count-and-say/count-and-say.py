class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        while n > 1:
            next = ''
            i = 0
            while i < len(s):
                char, count = self.get_num_count(s[i:])
                next += (str(count) + char)
                i += count
            s = next
            n -= 1
        return s

    def get_num_count(self, s):
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
            else:
                return s[i], i + 1

print(Solution().countAndSay(20))