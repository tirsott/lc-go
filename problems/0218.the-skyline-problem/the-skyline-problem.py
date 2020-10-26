from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        res = []
        for building in buildings:
            res = self.insert(res, building)
        for i in range(len(res)-1, -1, -1):
            if res[i][0] == res[i][1]:
                res.pop(i)
        for i in range(len(res) - 1, -1, -1):
            if i > 0 and res[i][0] == res[i-1][1] and res[i][2] == res[
                i-1][2]:
                res[i-1][1] = res[i][1]
                res.pop(i)
        skyline = []
        for i in range(len(res)):
            if i == 0:
                skyline.append([res[i][0], res[i][2]])
            else:
                if res[i][0] == res[i-1][1]:
                    skyline.append([res[i][0], res[i][2]])
                else:
                    skyline.append([res[i-1][1], 0])
                    skyline.append([res[i][0], res[i][2]])
        skyline.append([res[-1][1], 0])
        return skyline

    def insert(self, exists, next):
        if not exists or next[0] >= exists[-1][1]:
            exists.append(next)
            return exists
        else:
            for i in range(len(exists)):
                if exists[i][1] > next[0] >= exists[i][0] and next[1] <= \
                        exists[i][1]:
                    if next[2] <= exists[i][2]:
                        return exists
                    else:
                        right = exists[i][1]
                        exists[i][1] = next[0]
                        exists.insert(i+1, next)
                        exists.insert(i+2, [next[1], right, exists[i][2]])
                        return exists
                elif exists[i][1] > next[0] >= exists[i][0] and next[1] > \
                        exists[i][1]:
                    if next[2] <= exists[i][2]:
                        return self.insert(exists, [exists[i][1], next[1],
                                                    next[2]])
                    else:
                        right = exists[i][1]
                        exists[i][1] = next[0]
                        exists.insert(i + 1, [next[0], right, next[2]])
                        return self.insert(exists, [right, next[1], next[2]])



# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
#
# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。
# print(Solution().getSkyline([[0,2147483647,2147483647]]))
print(Solution().getSkyline([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]

))