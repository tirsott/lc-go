class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.temp = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.temp:
            return self.temp[0]
        self.temp.append(self.iterator.next())
        return self.temp[-1]

    def next(self):
        """
        :rtype: int
        """
        if self.temp:
            return self.temp.pop(0)
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.temp:
            return True
        return self.iterator.hasNext()