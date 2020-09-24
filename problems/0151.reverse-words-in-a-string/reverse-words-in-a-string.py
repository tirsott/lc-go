class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split(' ')
        return ' '.join([word for word in word_list[::-1] if word])


print(Solution().reverseWords("a good   example"))