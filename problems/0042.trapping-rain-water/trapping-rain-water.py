from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height) - 1):
            if min(max(height[0:i]), max(height[i+1:])) - height[i] > 0:
                res += min(max(height[0:i]), max(height[i+1:])) - height[i]
        return res

        return sum([min(max(height[0:i]), max(height[i+1:])) - height[i] for
                    i in range(1, len(height) - 1) if min(max(height[0:i]), max(height[i+1:])) -height[i] > 0])


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
