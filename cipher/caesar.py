from util import text
from util import codec


class Caesar:
    def __init__(self, n):
        self.n = n

    def encrypt(self, s):
        res = ""

        for i in range(len(s)):
            if text.is_letter(s[i]):
                # convert letter to code
                x = codec.to_number(s[i])

                # process
                x = (x + self.n) % 26

                # convert code to letter
                res += codec.to_letter(x)

            else:
                res += s[i]

        return res

    def decrypt(self, s):
        res = ""
        for i in range(len(s)):
            if text.is_letter(s[i]):
                # convert letter to code
                x = codec.to_number(s[i])

                # process
                x = (x - self.n) % 26

                # convert code to letter
                res += codec.to_letter(x)

            else:
                res += s[i]

        return res
