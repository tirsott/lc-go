class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        left = []
        res = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            else:
                if left:
                    res[i], res[left.pop()] = 1, 1
        maxlen = 0
        start = 0
        while start < len(s) and len(s) - start > maxlen:
            length = 0
            while start < len(s) and res[start] == 1:
                length += 1
                start += 1
            maxlen = max(length, maxlen)
            start += 1

        return maxlen

if __name__ == '__main__':
    print(Solution().longestValidParentheses( ")()())"))