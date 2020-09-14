from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                continue
            if stack and heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    left = stack.pop()
                    res = max(heights[left] * (i - stack[-1]-1), res)
                stack.append(i)
        return res


print(Solution().largestRectangleArea([4,2,0,3,2,5]))
