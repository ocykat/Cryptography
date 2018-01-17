from util import text
from util import codec


def encrypt(s, n):
    res = ""
    for i in range(len(s)):
        if text.is_letter(s[i]):
            x = codec.to_number(s[i])
            x = (x + n) % 26
            res += codec.to_letter(x)
        else:
            res += s[i]
    return res


def decrypt(s, n):
    res = ""
    for i in range(len(s)):
        if text.is_letter(s[i]):
            x = codec.to_number(s[i])
            x = (x - n) % 26
            res += codec.to_letter(x)
        else:
            res += s[i]
    return res
