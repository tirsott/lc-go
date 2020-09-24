from  typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num0 = stack.pop()
                if token == '+':
                    stack.append(num0 + num1)
                if token == '-':
                    stack.append(num0 - num1)
                if token == '*':
                    stack.append(num0 * num1)
                if token == '/':
                    stack.append(int(num0 / num1))
        return stack[0]


# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))