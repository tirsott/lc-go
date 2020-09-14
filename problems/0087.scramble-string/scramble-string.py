class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.str_has_same_char(s1[:i], s2[:i]):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(
                    s1[i:], s2[i:]):
                    return True
            elif self.str_has_same_char(s1[:i], s2[len(s1)-i:]):
                if self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(
                    s1[i:], s2[:len(s1)-i]):
                    return True
        return False

    def str_has_same_char(self, s1, s2):
        return sorted(s1) == sorted(s2)


print(Solution().isScramble('abcdbdacbdac', 'bdacabcdbdac'))
# "abcdbdacbdac"
# "bdacabcdbdac"
# great rgeat
# abcde caebd
