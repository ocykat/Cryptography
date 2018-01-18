def to_number(c):
    return ord(c) - ord('a')


def to_letter(n):
    return chr(n + ord('a'))


def is_letter(c):
    if ord('A') <= ord(c) <= ord('Z'):
        return True
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False
