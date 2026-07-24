class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            length = len(word)
            piece = str(length) + "#" + word

            result = result + piece

        return result

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):
            pos = s.find("#",i)
            length = int(s[i:pos])
            word = s[pos+1 : pos+1+length]

            result.append(word)

            i = pos + 1 + length

        return result
