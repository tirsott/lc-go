class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.nums.sort()


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.nums) < 2:
            return False
        left, right = 0, len(self.nums) - 1
        while left < right:
            if self.nums[left] + self.nums[right] == value:
                return True
            elif self.nums[left] + self.nums[right] < value:
                left += 1
            else:
                right -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)