class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        if E >= C or G <= A or F >= D or H <= B:
            return area1 + area2
        if A in range(E, G+1) and C in range(E, G+1):
            crossx = (C - A)
        elif A in range(E, G+1) and C > G:
            crossx = (G - A)
        elif C in range(E, G+1) and A < E:
            crossx = (C - E)
        elif C > G and A < E:
            crossx = (G - E)
        if B in range(F, H+1) and D in range(F, H+1):
            crossy = (D - B)
        elif B in range(F, H+1) and D > H:
            crossy = (H - B)
        elif D in range(F, H+1) and B < F:
            crossy = (D - F)
        elif D > H and B < F:
            crossy = (H - F)
        return area1 + area2 - crossx * crossy





# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
