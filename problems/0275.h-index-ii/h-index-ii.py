from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        l = len(citations)
        res = 0
        start = l // 2
        for i in range(start+1):
            if start + i < l:
                res = max(min(l - (start + i), citations[start + i]), res)
            if start - i >= 0:
                res = max(min(l - (start - i), citations[start - i]), res)
            if res >= l - start and citations[start-i] <= res:
                return res
        return res