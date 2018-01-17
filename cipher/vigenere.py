from util import text
from util import codec


class Vigenere:
    def __init__(self, keyword):
        self.keyword = keyword

    def encrypt(self, s):
        res = ""
        key_char_index = 0

        for i in range(len(s)):
            if text.is_letter(s[i]):
                # convert letter to code
                x = codec.to_number(s[i])

                # process
                key_char = self.keyword[key_char_index]
                k = codec.to_number(key_char)
                x = (x + k) % 26

                # convert code to letter
                res += codec.to_letter(x)

                # update key_char_index
                key_char_index += (key_char_index + 1) % len(self.keyword)
            else:
                res += s[i]
        return res

    def decrypt(self, s):
        res = ""
        key_char_index = 0

        for i in range(len(s)):
            if text.is_letter(s[i]):
                # convert letter to code
                x = codec.to_number(s[i])

                # process
                key_char = self.keyword[key_char_index]
                k = codec.to_number(key_char)
                x = (x - k) % 26

                # convert code to letter
                res += codec.to_letter(x)

                # update key_char_index
                key_char_index += (key_char_index + 1) % len(self.keyword)
            else:
                res += s[i]
        return res
