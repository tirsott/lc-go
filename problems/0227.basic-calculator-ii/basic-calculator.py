class Solution:
    def calculate(self, s: str) -> int:
        s.replace(' ', '')
        i = 0
        operator = '+'
        res = 0
        while i < len(s):
            if s[i] in '+-':
                operator = s[i]
                i += 1
                continue
            else:
                start = i
                while i < len(s) - 1 and s[i+1] not in '+-':
                    i += 1
                if operator == '+':
                    res += self.cal_str(s[start:i+1])
                else:
                    res -= self.cal_str(s[start:i + 1])
                i += 1
        return res

    def cal_str(self, s):
        if s.isdigit():
            return int(s)
        stack = []
        i = 0
        while i < len(s):
            if s[i] in '*/':
                stack.append(s[i])
            else:
                start = i
                while i < len(s) - 1 and s[i+1] not in '*/':
                    i += 1
                if not stack:
                    stack.append(int(s[start:i+1]))
                elif stack[-1] == '*':
                    stack.pop()
                    stack[-1] = stack[-1] * int(s[start:i+1])
                elif stack[-1] == '/':
                    stack.pop()
                    stack[-1] = stack[-1] // int(s[start:i+1])
            i+= 1
        return stack[0]



# 示例 3:
#
# 输入: " 3+5 / 2 "
# 输出: 5
s = " 3+5 / 2 "
print(Solution().calculate(s))