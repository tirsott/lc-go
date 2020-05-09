class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.strip("/").split("/")
        stack = []
        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                pass
            else:
                stack.append(i)
        return "/" + "/".join(stack)


print(Solution().simplifyPath("/."))