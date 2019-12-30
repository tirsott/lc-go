class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while index < len(haystack) - len(needle) + 1:
            if haystack[index:index+(len(needle))] == needle:
                return index
            else:
                match = self.get_str_match(haystack[index:index+(len(
                    needle))], needle)
                index += match
        return -1



    def get_str_match(self, a, b):
        for i in range(len(a)):
            if a[i:] == b[:len(a)-i]:
                return i
        return len(a)


if __name__ == '__main__':
    # print(Solution().strStr('aaaaa', 'bba'))
    # print(Solution().strStr('hello', 'll'))
    print(Solution().strStr("mississippi", 'issi'))