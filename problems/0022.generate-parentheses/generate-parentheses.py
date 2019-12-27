from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(combination, left_count, right_count):
            if len(combination) == 2 * n:
                res.append(combination)
                return
            if left_count < n:
                backtrack(combination + '(', left_count + 1, right_count)
            if right_count < left_count:
                backtrack(combination + ')', left_count, right_count + 1)
        backtrack('', 0, 0)
        return res

if __name__ == '__main__':
    print(Solution().generateParenthesis(2))