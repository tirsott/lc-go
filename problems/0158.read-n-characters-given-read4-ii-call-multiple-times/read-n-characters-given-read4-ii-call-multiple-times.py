# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        self.cache = []

    def read(self, buf: List[str], n: int) -> int:

        while n > len(self.cache):
            data = [''] * 4
            size = read4(data)
            if size > 0:
                self.cache.extend(data[:size])
            else:
                break
        ret = len(self.cache[:n])
        for i in range(ret):
            buf[i] = self.cache[i]

        self.cache = self.cache[n:]

        return ret
