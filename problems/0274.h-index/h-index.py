from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        res = 0
        for i in range(l):
            res = max(min(l-i, citations[i]), res)
        return res



# 示例：
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
#      由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
#