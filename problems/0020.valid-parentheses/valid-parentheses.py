class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif item == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif item == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(item)
        return stack == []

if __name__ == '__main__':
    print(Solution().isValid("{[]}"))