from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if not digits:
            return res
        def recursive(combination, next_digits):
            if not next_digits:
               res.append(combination)
               return
            for char in mapping[next_digits[0]]:
                recursive(combination+char, next_digits[1:])
        recursive('', digits)
        return res

if __name__ == '__main__':
    print(Solution().letterCombinations(''))