from util import text

def say_hello():
    print("hello world")

def encode(s, n):
    res = ""
    for i in range(len(s)):
        if text.isLetter(s[i]):
            x = ord(s[i]) - ord('a')
            x = (x + n) % 26
            x += ord('a')
            res += chr(x)
        else:
            res += s[i]
    return res

def decode(s, n):
    res = ""
    for i in range(len(s)):
        if text.isLetter(s[i]):
            x = ord(s[i]) - ord('a')
            x = (x - n) % 26
            x += ord('a')
            res += chr(x)
        else:
            res += s[i]
    return res
