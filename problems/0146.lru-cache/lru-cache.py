class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.used = []

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.used.remove(key)
            self.used.append(key)
            return self.mapping[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key] = value
            self.used.remove(key)
            self.used.append(key)
        else:
            if len(self.mapping) < self.capacity:
                self.mapping[key] = value
                self.used.append(key)
            else:
                del self.mapping[self.used.pop(0)]
                self.mapping[key] = value
                self.used.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(2)

cache.put(1, 1)
print(cache.mapping, cache.used)
cache.put(2, 2)
print(cache.mapping, cache.used)
cache.get(1)
print(cache.mapping, cache.used)
cache.put(3, 3)
print(cache.mapping, cache.used)
cache.get(2)
print(cache.mapping, cache.used)
cache.put(4, 4)
print(cache.mapping, cache.used)
cache.get(1)
print(cache.mapping, cache.used)
cache.get(3)
print(cache.mapping, cache.used)
cache.get(4)
print(cache.mapping, cache.used)
