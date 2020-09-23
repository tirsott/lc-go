from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        res_left = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res_left[i] = res_left[i-1] + 1
        res_right = [1 for _ in range(len(ratings))]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res_right[i] = res_right[i+1] + 1

        res = [max(res_left[i], res_right[i]) for i in range(len(ratings))]
        return sum(res)

# [1,0,2]
print(Solution().candy([1,3,2,2,1]))