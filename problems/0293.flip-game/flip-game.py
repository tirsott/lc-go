from typing import List

class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '+':
               res.append(s[:i] + '--' + s[i+2:])
        return res