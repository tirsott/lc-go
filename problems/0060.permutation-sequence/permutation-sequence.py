class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        res = []
        nums = [i for i in range(1, n+1)]
        while len(res) < n:
            if len(nums) == 1:
                res.append(nums[0])
                break
            for i in range(len(nums)):
                if math.factorial(len(nums)-1) * (i+1) >= k:
                    res.append(nums[i])
                    k -= i * math.factorial(len(nums) - 1)
                    nums.pop(i)
                    break
        return ''.join([str(x) for x in res])



print(Solution().getPermutation(4, 4))
