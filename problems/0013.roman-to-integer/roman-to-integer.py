class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        if not s:
            return res
        last = s[-1]
        for char in reversed(s):
            if mapping[char] < mapping[last]:
                res -= mapping[char]
            else:
                res += mapping[char]
                last = char
        return res

if __name__ == '__main__':
    print(Solution().romanToInt('IV'))