class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = []
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                bulls.append(i)
                secret = secret[:i] + secret[i+1:]
                guess = guess[:i] + guess[i+1:]
            else:
                i += 1
        d_secret = {x: secret.count(x) for x in secret}
        d_guess = {x: guess.count(x) for x in guess}
        res = {x: min(d_guess[x], d_secret[x]) for x in d_guess if x in d_secret}
        return f"{len(bulls)}A{sum(res.values())}B"

print(Solution().getHint(secret = "1122", guess = "2211"))

# 示例 1:
#
# 输入: secret = "1807", guess = "7810"
# 输出: "1A3B"
# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
#
# 示例 2:
#
# 输入: secret = "1123", guess = "0111"
# 输出: "1A1B"
# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
#
