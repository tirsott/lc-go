from typing import List

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = [l for l in v if l]

    def next(self) -> int:
        next = self.v[0].pop(0)
        if not self.v[0]:
            self.v.pop(0)
        return next

    def hasNext(self) -> bool:
        return True if self.v and self.v[0] else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()