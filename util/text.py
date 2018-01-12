def isLetter(c):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return True
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
