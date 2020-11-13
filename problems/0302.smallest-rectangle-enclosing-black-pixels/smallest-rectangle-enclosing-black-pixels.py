from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image:
            return 0
        top, left, right, bottom = -1, -1, -1, -1
        for i in range(len(image)):
            if '1' in image[i]:
                top = i
                break
        for i in range(len(image)-1, -1, -1):
            if '1' in image[i]:
                bottom = i
                break
        for i in range(len(image[0])):
            if '1' in [x[i] for x in image]:
                left = i
                break
        for i in range(len(image[0])-1, -1, -1):
            if '1' in [x[i] for x in image]:
                right = i
                break
        if top == -1:
            return 0
        return (right-left+1) * (bottom-top+1)

# 输入:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# 和 x = 0, y = 2
#
# 输出: 6