class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(['!@#$%$#@!'+s for s in strs])




    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        while s.startswith('!@#$%$#@!'):
            s = s[9:]
            next = s.index('!@#$%$#@!') if '!@#$%$#@!' in s else len(s)
            res.append(s[:next])
            s = s[next:]
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))