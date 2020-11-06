from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.next_v = -1
        for i in range(len(self.v)):
            if self.v[i]:
                self.next_v = i
                break

    def next(self) -> int:
        next = self.v[self.next_v].pop(0)
        for i in range(1, len(self.v)+1):
            if self.v[(self.next_v+i)%len(self.v)]:
                self.next_v = (self.next_v+i)%len(self.v)
                break
        return next

    def hasNext(self) -> bool:
        for x in self.v:
            if x:
                return True
        return False

z = ZigzagIterator([1,2], [3,4,5,6])
while z.hasNext():
    print(z.next())



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())